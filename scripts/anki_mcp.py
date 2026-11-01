#!/usr/bin/env python3
"""Call the Anki MCP Server addon over HTTP, without registering it as an MCP server.

  anki_mcp.py tools                 server instructions, then one line per tool
  anki_mcp.py schema <tool>         a tool's full description and input schema
  anki_mcp.py call <tool> [JSON]    call a tool; JSON arguments as an argument,
                                    from stdin with "-", or from a file with "@path"

A call prints the tool's result as JSON and exits 0, or exits 1 when the tool
or the server reports an error. Exit 2 means the server could not be reached, 3 means the
request was sent but no answer arrived (an uncertain write), 4 is a usage error.

Environment: ANKI_MCP_URL (default http://127.0.0.1:3141/), ANKI_MCP_API_KEY
(the addon's http_api_key, when set), ANKI_MCP_TIMEOUT (seconds, default 60).
"""

import json
import os
import sys
import urllib.error
import urllib.request

URL = os.environ.get("ANKI_MCP_URL", "http://127.0.0.1:3141/")
API_KEY = os.environ.get("ANKI_MCP_API_KEY", "")
TIMEOUT = float(os.environ.get("ANKI_MCP_TIMEOUT", "60"))
PROTOCOL = "2025-03-26"


class Unreachable(Exception):
    pass


class NoAnswer(Exception):
    pass


class Failed(Exception):
    pass


def post(message, session=None):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if API_KEY:
        headers["Authorization"] = "Bearer " + API_KEY
    if session:
        headers["Mcp-Session-Id"] = session
    request = urllib.request.Request(URL, json.dumps(message).encode(), headers)
    try:
        response = urllib.request.urlopen(request, timeout=TIMEOUT)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:500]
        raise Unreachable(f"HTTP {e.code} from {URL}: {body}") from None
    except TimeoutError:
        raise NoAnswer(f"no answer from {URL} within {TIMEOUT:g}s") from None
    except (urllib.error.URLError, ConnectionError) as e:
        if isinstance(getattr(e, "reason", None), TimeoutError):
            raise NoAnswer(f"no answer from {URL} within {TIMEOUT:g}s") from None
        raise Unreachable(
            f"cannot reach {URL} ({getattr(e, 'reason', e)}): "
            "is Anki open with the Anki MCP Server addon enabled?"
        ) from None
    try:
        with response:
            session = response.headers.get("Mcp-Session-Id") or session
            body = response.read().decode()
    except TimeoutError:
        raise NoAnswer(f"no answer from {URL} within {TIMEOUT:g}s") from None
    # The server answers with plain JSON or with server-sent events.
    if response.headers.get_content_type() == "text/event-stream":
        data = [line[5:].strip() for line in body.splitlines() if line.startswith("data:")]
        body = data[-1] if data else ""
    return (json.loads(body) if body.strip() else None), session


def rpc(method, params):
    hello, session = post({
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {
            "protocolVersion": PROTOCOL,
            "capabilities": {},
            "clientInfo": {"name": "anki-skill", "version": "1"},
        },
    })
    post({"jsonrpc": "2.0", "method": "notifications/initialized"}, session)
    reply, _ = post({"jsonrpc": "2.0", "id": 2, "method": method, "params": params}, session)
    if reply is None:
        raise NoAnswer(f"empty answer to {method}")
    if "error" in reply:
        raise Failed(f"{method} failed: {reply['error'].get('message', reply['error'])}")
    return hello["result"], reply["result"]


def list_tools():
    hello, result = rpc("tools/list", {})
    if hello.get("instructions"):
        print(hello["instructions"].strip(), end="\n\n")
    for tool in result["tools"]:
        summary = (tool.get("description") or "").strip().split("\n")[0]
        print(f"{tool['name']}: {summary}")
    return 0


def show_schema(name):
    _, result = rpc("tools/list", {})
    for tool in result["tools"]:
        if tool["name"] == name:
            print(json.dumps(tool, indent=1))
            return 0
    print(f"no tool named {name!r}; run `tools` for the list", file=sys.stderr)
    return 4


def call_tool(name, raw):
    if raw == "-":
        raw = sys.stdin.read()
    elif raw.startswith("@"):
        with open(raw[1:]) as f:
            raw = f.read()
    try:
        arguments = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"arguments are not valid JSON: {e}", file=sys.stderr)
        return 4
    _, result = rpc("tools/call", {"name": name, "arguments": arguments})
    if "structuredContent" in result:
        output = result["structuredContent"]
    else:
        text = "\n".join(c.get("text", "") for c in result.get("content", []))
        try:
            output = json.loads(text)
        except json.JSONDecodeError:
            output = text
    print(output if isinstance(output, str) else json.dumps(output, indent=1, ensure_ascii=False))
    return 1 if result.get("isError") else 0


def main(argv):
    try:
        if argv[:1] == ["tools"] and len(argv) == 1:
            return list_tools()
        if argv[:1] == ["schema"] and len(argv) == 2:
            return show_schema(argv[1])
        if argv[:1] == ["call"] and len(argv) in (2, 3):
            return call_tool(argv[1], argv[2] if len(argv) == 3 else "{}")
    except Failed as e:
        print(e, file=sys.stderr)
        return 1
    except Unreachable as e:
        print(e, file=sys.stderr)
        return 2
    except ValueError as e:
        print(f"unreadable answer from {URL}: {e}", file=sys.stderr)
        return 2
    except NoAnswer as e:
        print(f"{e}. A write may or may not have happened: check before retrying.", file=sys.stderr)
        return 3
    print(__doc__.strip(), file=sys.stderr)
    return 4


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

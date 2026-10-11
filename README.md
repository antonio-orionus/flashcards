# Generating STEM Flashcards

An agent skill for creating concise STEM and probability flashcards from notes, textbooks, worksheets, or a topic. This fork of [jalliet/flashcards](https://github.com/jalliet/flashcards) preserves its three-layer approach and adds beginner-friendly English, one-step numerical examples, labeled diagrams, and duplicate-aware Anki creation.

## Agent Compatibility

The card-writing instructions are Markdown in `SKILL.md`, with supporting references. They are not tied to a particular model provider. The [skills CLI](https://github.com/vercel-labs/skills) can install them for supported agents, including Claude Code, Codex, Cursor, and others.

Installation and runtime capabilities are separate: an agent still needs access to the tools required by the selected output mode. Installing a skill does not install Anki, connect an MCP server, or provide a React artifact viewer.

| Output | Required capabilities |
|--------|-----------------------|
| Anki-ready TSV | Write a text file; include media files for diagram cards |
| Direct Anki creation | Access to the configured Anki MCP Server addon, with Anki running |
| Interactive React artifact | A host or application capable of running the supplied React/KaTeX component; this is an optional output with host-specific requirements |

The upstream project was originally documented for Claude, so its [public interactive example](https://claude.ai/public/artifacts/6c97797f-3b9d-4245-a5b5-5a4d5da02fcf) uses Claude's artifact viewer. The Anki and TSV workflows do not depend on that viewer. The supplied React template supports text and math; diagrams require an image-capable output or an adapted template.

## Installation

Install this fork using the cross-agent installer. Choose one command for the package manager you use:

| Package manager | Install command |
|-----------------|-----------------|
| npm | `npx skills add antonio-orionus/flashcards --skill generating-stem-flashcards` |
| [Bun](https://bun.com/docs/pm/bunx) | `bunx skills add antonio-orionus/flashcards --skill generating-stem-flashcards` |
| [pnpm](https://pnpm.io/cli/dlx) | `pnpm dlx skills add antonio-orionus/flashcards --skill generating-stem-flashcards` |
| [Yarn (modern)](https://yarnpkg.com/cli/dlx) | `yarn dlx skills add antonio-orionus/flashcards --skill generating-stem-flashcards` |

Choose your agent in the installer. See the [CLI documentation](https://github.com/vercel-labs/skills#options) for selecting agents and choosing project or global installation.

For an environment without the installer, use its supported skill-loading mechanism to load `SKILL.md` together with the `references/`, `anki/`, and `artifact/` resources it links to. The upstream release packages contain the original project's instructions, rather than this fork's adaptations.

## Card Design

| Layer | Tests | Probability example |
|-------|-------|---------------------|
| L1: Recall | Definitions and notation | What does P(A\|B) mean? |
| L2: Understanding | Intuition, interpretation, and one-step applications | A fair die shows an even number. What is the probability it shows 6? |
| L3: Boundaries | Conditions, limitations, and misconceptions | Can two mutually exclusive events with positive probabilities be independent? |

Each card asks one self-contained question. The back gives the answer first, with a brief explanation when useful. Small numerical examples and labeled geometry diagrams support understanding; extended proofs and worked problems remain separate practice. Mathematical notation uses Anki's MathJax delimiters for Anki output and client-side KaTeX for the React component.

See [beginner STEM guidance](references/BEGINNER_STEM.md), [atomicity rules](references/ATOMICITY.md), [cognitive layers](references/COGNITIVE_LAYERS.md), and [the theoretical background](Theory.md).

## Usage

Provide the source material or specify the topic, level, language, and desired output. For example:

> Create about 40 beginner English probability cards. Include notation, short dice examples, and area diagrams. Add them to my Probability — Foundations deck through the connected Anki MCP, checking existing notes first.

> Export these cards as an Anki-ready TSV file with any diagram media.

> Add conceptual cards about independence. Avoid duplicating my existing cards.

> Correct the conditional-probability answer on the existing card.

Keep course material together in whatever workspace or project your agent supports. PDF or document-reading tools can help with source extraction, but are not required for pasted text or topic-based requests.

## Anki Connection and Outputs

### Direct Creation Through MCP

Use the [Anki MCP Server addon](https://github.com/ankimcp/anki-mcp-server-addon) with the MCP client configuration supported by your agent. The addon normally listens at `http://127.0.0.1:3141/` while Anki is running. Reuse an established connection rather than setting up another integration.

The skill inspects the target deck and existing notes, reuses a compatible Front/Back note type, and stores layer/topic metadata in tags. A custom `3-Layer Card` note type is optional. It skips equivalent cards, reads back new notes, and reconciles uncertain writes before retrying. See [the MCP workflow](anki/MCP_WORKFLOW.md) for the current tool arguments and verification steps.

If the connection fails, check that Anki is running, the addon is enabled, and the agent exposes its tools. Consult your client's current MCP documentation and the [addon documentation](https://github.com/ankimcp/anki-mcp-server-addon) for transport configuration; a bridge is only needed when the client requires one. Skill installation alone does not establish the connection.

### TSV Export

See [the TSV workflow](anki/WORKFLOW.md) and [import guide](anki/IMPORT_GUIDE.md). The export can be mapped to an existing Basic Front/Back note type, with layer/topic information in tags, or to the optional custom model described in [the note template](anki/NOTE_TYPE_TEMPLATE.md). Include referenced diagram media with the export.

### Optional Interactive Output

See [the React artifact workflow](artifact/WORKFLOW.md) and [template](artifact/template.jsx). Use this mode where the host can run the component. A saved `.jsx` file alone is not a working interactive viewer in every agent.

## Validation

[Behavior scenarios](tests/SCENARIOS.md) cover beginner probability examples, existing Basic notes with formatted duplicate fronts, and reconciliation after a write timeout. The recorded comparison uses simulations, not live Anki writes. Validation does not certify every output mode or every agent integration.

## License

MIT, as stated by the upstream project.

# Anki MCP Direct Push Workflow

Continue after the shared workflow in `SKILL.md`. This guide targets the Anki MCP Server addon (`124672614`, normally `http://127.0.0.1:3141/`). Anki must be running. Use the connected tool descriptions as the authority for names, arguments, and response shapes; examples below use the current snake_case API, not AnkiConnect's camelCase API.

## Inspect Before Writing

1. Call `list_decks` and confirm the exact requested deck. Create it only if absent, using `create_deck({"deck_name": "<target>"})`.
2. Inspect existing notes with `find_notes({"query": "deck:\"Probability — Foundations\"", "limit": 500, "offset": 0})`. Quote and escape the user's deck name using Anki search syntax. Continue pagination until all target notes are loaded; a page limit is not the collection's size.
3. Fetch full Front/Back values using `notes_info({"notes": [101], "include_fields": ["Front", "Back"]})` in manageable batches. Do not use truncated excerpts for matching or updates.
4. List note types with `model_names({})` and inspect compatible fields with `model_field_names({"model_name": "Basic"})`. Reuse the user's existing compatible Front/Back model. Put layer/topic metadata in tags when those fields do not exist. Do not automatically change templates or CSS shared by existing cards.

If a custom `3-Layer Card` model is requested, use its existing fields after checking them. If it is missing, create it with `model_name`, `in_order_fields: ["Front", "Back", "Layer", "Topic"]`, and `card_templates: [{"Name": "Card 1", "Front": "<front template>", "Back": "<back template>"}]`, using [NOTE_TYPE_TEMPLATE.md](NOTE_TYPE_TEMPLATE.md) for HTML/CSS. Do not create a custom model merely to hold layer metadata.

## Plan New Cards and Duplicates

Compare every proposed front against both existing target-deck notes and the current batch. Ignore presentation-only differences such as bold HTML, equivalent entities, and repeated whitespace. Retain mathematical symbols, meaningful punctuation/case, and image references when comparing. Also check for paraphrases testing the same idea in the same example; retain variants that deliberately test a different cognitive task.

- Existing equivalent card: skip it and count it as a duplicate. Adding cards does not imply rewriting an existing answer.
- Explicit correction request: identify the exact existing note, read its full fields, and use `update_note_fields` or `update_notes` under the current schema; preserve unrelated fields and review history.
- New question: prepare an addition using the inspected model.

## Prepare Math and Media

Keep LaTeX as text wrapped in `\(...\)` or `\[...\]`; Anki renders it using MathJax. See [RENDERING.md](RENDERING.md).

For a generated diagram, inspect the labels, geometry, and answer first. Use a descriptive filename with a content hash to avoid overwriting unrelated media. Upload with `store_media_file({"filename": "probability_area_<hash>.svg", "path": "<absolute local path>"})`. Reference the returned filename, for example `<img src="<returned filename>" alt="B has area 6; its overlap with A has area 2">`. Required diagram information belongs on the front; the answer belongs on the back. Verify that every referenced file was stored successfully.

## Add, Reconcile, and Verify

For each new Basic note, use the live schema, for example:

```json
{
  "deck_name": "Probability — Foundations",
  "model_name": "Basic",
  "fields": {
    "Front": "A fair die shows an even number. What is the probability it shows 6?",
    "Back": "1/3. The possible even results are 2, 4, and 6; one is 6."
  },
  "tags": ["STEM", "L2-Understanding", "ConditionalProbability"],
  "allow_duplicate": false
}
```

Send only fields that exist in the chosen model. Inspect each result for success/errors and record returned note IDs; batch operations may partially succeed. Keep duplicate prevention enabled, and check additions within the current batch as well as against the initial inventory.

A timeout after sending is an **uncertain write**, not proof of failure. Before retrying, query the target deck again and inspect candidates' full fields. If the intended card exists, recover its note ID and verify it. Retry only after a successful reconciliation shows it absent. If the connection prevents reconciliation, stop further writes, preserve the uncertain operation, and report it; do not blindly resend or suggest importing the same batch.

Read back created/updated notes with `notes_info` and compare the requested fields and media references. Separate verified note counts from card counts, since some models generate multiple cards per note. Report actual verified additions, duplicate skips, updates, confirmed failures, and unresolved writes. A deck's total count alone does not verify the batch.

## Existing Connection and Iteration

Use the established integration rather than installing or reconfiguring another server. If tools are missing or calls fail, report that observed condition and provide a TSV/media alternative when direct creation cannot be completed. Sync is separate: when the user uses AnkiWeb across devices, offer sync at the start/end; call it only when authorized, never implicitly.

For requested additions, repeat inspection and duplicate planning. For corrections, update the identified note rather than adding a replacement. For removals, identify the intended notes and follow the user's deletion authorization. Open the target deck in Anki only when useful or requested, using the available GUI tools.

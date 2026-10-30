---
name: anki
description: "Use for any Anki work: making flashcards or revision cards from notes, textbooks, worksheets or a topic (STEM and probability cards with math notation, small numerical examples and diagrams get a dedicated method), adding cards to Anki or exporting them for import, and managing a collection through the Anki MCP Server addon: searching, editing, tagging, moving, suspending or deleting notes and cards, creating decks, reviewing due cards, and syncing with AnkiWeb."
---

# Anki

## Pick the Task

| Request | Path |
|---|---|
| Cards on a STEM topic: math, physics, probability, CS theory, anything with notation or worked numbers | **STEM cards**: Shared Workflow below, then an output mode |
| Cards on anything else: vocabulary, history, facts, definitions | **General cards**: [General Cards](#general-cards), then an output mode |
| Search, edit, tag, move, suspend, delete, create decks, review, sync | **Manage**: [anki/MANAGE.md](anki/MANAGE.md) |

## Output Mode Detection

Detect the output mode from the user's request:

**Anki mode (MCP direct)**: "add to anki", "send to anki", "push to anki", "create in anki", "put in my deck"
**Anki mode (TSV export)**: "anki export", "import into anki", "anki file", "tsv"
**Artifact mode**: "interactive", "artifact", "study cards" without mentioning Anki

Use the user's requested format and established session preferences. For Anki requests with an available, working Anki MCP, use direct push. If MCP is unavailable, explain the actual connection result and provide an Anki-ready export. Ask about format only when the choice is unresolved.

## Dependencies

### Anki mode (MCP direct) and Manage
Requires:
- **Anki 25.x or later** running locally
- **Anki MCP Server addon** installed (code: `124672614`)
  Install: Tools → Add-ons → Get Add-ons → enter `124672614` → restart Anki
- Server auto-starts on `http://127.0.0.1:3141/` when Anki opens

The connected tool descriptions are the authority for names and arguments. This skill targets that addon's snake_case tools (`find_notes`, `add_notes`, `tag_management`), not AnkiConnect's camelCase API or other servers' `anki_*` tools.

### Anki mode (TSV export)
No dependencies required (uses raw LaTeX with MathJax delimiters).

### Artifact mode
No CLI dependencies required. The React artifact handles KaTeX rendering client-side. It needs a host that can run the component.

**Recommended complementary skills** from [anthropics/skills](https://github.com/anthropics/skills):
- `frontend-design` — Improved React artifact rendering and styling
- `pdf` — Better extraction from scanned/complex PDFs
- `docx` — Preserves formatting from Word documents

---

## Shared Workflow (STEM Cards)

### Step 1: Extract Topics
Identify topic boundaries from section headings or conceptual groupings.
Respect the requested level, language, scope, and card count. Use plain English by default; follow a different language if requested. For beginner material, small numerical examples, or geometry, read [references/BEGINNER_STEM.md](references/BEGINNER_STEM.md).

### Step 2: Generate Cards
For each topic, create cards across three layers:
- **L1 (Recall)**: Facts, definitions, formulas
- **L2 (Understanding)**: Why/how, connections, intuition, one-step application
- **L3 (Boundaries)**: Limitations, edge cases, when things break

See `references/COGNITIVE_LAYERS.md` for layer definitions, card types, and answer constraints.

### Step 3: Validate Cards
Check each card against atomicity rules and refusal policy.

See `references/ATOMICITY.md` for atomicity definition, refusal policy, and quality checklist.

For LaTeX syntax lookup: `references/LATEX_SYNTAX.md`

---

## General Cards

For non-STEM material, skip the three layers and keep the atomicity rules from `references/ATOMICITY.md`: each card tests exactly one thing, and the front can be answered without seeing other cards.

| Note type | Fields | Use for |
|---|---|---|
| `Basic` | `Front`, `Back` | Definitions, facts, Q&A |
| `Basic (and reversed card)` | `Front`, `Back` | Vocabulary both ways |
| `Cloze` | `Text` with `{{c1::deletion}}`, optional `Back Extra` | Fill-in-the-blank, sequences, lists |

Field names vary between collections and languages, so confirm them with `model_field_names` before writing. Tag by topic, not by layer. A request for N cards means N notes; say so when a reversed type turns them into 2N cards.

Then continue with the chosen output mode. The MCP workflow's inspection, duplicate and verification steps apply unchanged. For a TSV export, drop the Layer and Topic columns and the layer tags: `#columns:Front	Back	Tags` mapped to Basic, or `Text	Back Extra	Tags` mapped to Cloze. Artifact mode is for STEM cards only, since its template requires a layer per card.

---

## Mode-Specific Workflow

After the card content is ready, branch based on the detected mode:

### → Anki Mode (MCP — Direct Push)

Read and follow `anki/MCP_WORKFLOW.md`. Summary:

1. Wrap LaTeX in MathJax delimiters (see `anki/RENDERING.md`)
2. Inspect the target deck, existing notes, and compatible note types
3. Add only new cards; reuse existing note types and upload diagram media when needed
4. Read back writes and report verified additions, duplicate skips, failures, and uncertain results

### → Anki Mode (TSV Export)

Read and follow `anki/WORKFLOW.md`. Summary:

1. Wrap LaTeX in MathJax delimiters (see `anki/RENDERING.md`)
2. Build 5-column TSV with per-card tags
3. Save to the workspace output directory (or the host's provided artifact directory)
4. Present draft with import instructions from `anki/IMPORT_GUIDE.md`

### → Artifact Mode

Read and follow `artifact/WORKFLOW.md`. Summary:

1. Write raw LaTeX strings (NOT compiled HTML)
2. Build artifact from `artifact/template.jsx`
3. Save to the workspace output directory (or the host's provided artifact directory)
4. Present draft

---

## Communication Style

Report progress in phases, not steps. Use compact formats:

```
Extracted 8 topics. Generating cards...

Draft: 45 cards (L1: 18, L2: 15, L3: 12). Review and let me know changes.
```

For iterations: "Updated card 12. ✓"

Omit rendering mechanics (KaTeX/MathJax) from user-facing messages.

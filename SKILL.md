---
name: generating-stem-flashcards
description: "Use when users request STEM or probability flashcards, Anki cards, or revision cards from notes, textbooks, worksheets, or a topic, especially when mathematical notation, conceptual understanding, small numerical examples, or diagrams matter."
---

# STEM Flashcard Generation

## Output Mode Detection

Detect the output mode from the user's request:

**Artifact mode** (default): "flashcards", "interactive", "artifact", "study cards", "revision cards"
**Anki mode (TSV export)**: "anki", "anki deck", "for anki", "import into anki", "anki export", "export to anki"
**Anki mode (MCP direct)**: "send to anki", "push to anki", "add to anki directly", "anki mcp", "create in anki"

Use the user's requested format and established session preferences. For Anki requests with an available, working Anki MCP, use direct push. If MCP is unavailable, explain the actual connection result and provide an Anki-ready export. Ask about format only when the choice is unresolved. Without an Anki request, default to artifact mode.

## Dependencies

### Artifact mode
No CLI dependencies required. The React artifact handles KaTeX rendering client-side.

**Recommended complementary skills** from [anthropics/skills](https://github.com/anthropics/skills):
- `frontend-design` — Improved React artifact rendering and styling
- `pdf` — Better extraction from scanned/complex PDFs
- `docx` — Preserves formatting from Word documents

### Anki mode (TSV export)
No dependencies required (uses raw LaTeX with MathJax delimiters).

### Anki mode (MCP direct)
Requires:
- **Anki 25.x or later** running locally
- **Anki MCP Server addon** installed (code: `124672614`)
  Install: Tools → Add-ons → Get Add-ons → enter `124672614` → restart Anki
- Server auto-starts on `http://127.0.0.1:3141/` when Anki opens

No file export or manual import needed — cards are pushed directly into Anki.

---

## Shared Workflow (All Modes)

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

## Mode-Specific Workflow

After completing Steps 1–3, branch based on the detected mode:

### → Artifact Mode

Read and follow `artifact/WORKFLOW.md`. Summary:

4. Write raw LaTeX strings (NOT compiled HTML)
5. Build artifact from `artifact/template.jsx`
6. Save to the workspace output directory (or the host's provided artifact directory)
7. Present draft

### → Anki Mode (TSV Export)

Read and follow `anki/WORKFLOW.md`. Summary:

4. Wrap LaTeX in MathJax delimiters (see `anki/RENDERING.md`)
5. Build 5-column TSV with per-card tags
6. Save to the workspace output directory (or the host's provided artifact directory)
7. Present draft with import instructions from `anki/IMPORT_GUIDE.md`

### → Anki Mode (MCP — Direct Push)

Read and follow `anki/MCP_WORKFLOW.md`. Summary:

4. Wrap LaTeX in MathJax delimiters (see `anki/RENDERING.md`)
5. Inspect the target deck, existing notes, and compatible note types
6. Add only new cards; reuse existing note types and upload diagram media when needed
7. Read back writes and report verified additions, duplicate skips, failures, and uncertain results

---

## Communication Style

Report progress in phases, not steps. Use compact formats:

```
Extracted 8 topics. Generating cards...

Draft: 45 cards (L1: 18, L2: 15, L3: 12). Review and let me know changes.
```

For iterations: "Updated card 12. ✓"

Omit rendering mechanics (KaTeX/MathJax) from user-facing messages.

# Skill Behavior Checks

Use these simulations after changing the card rules or MCP workflow. Perform no live Anki writes: provide drafts and planned calls using the current tool schemas. Skill frontmatter validation alone does not check these decisions.

## Beginner Probability

Request six concise English cards covering a fair-die conditional calculation, interpreting P(A|B), probability by area, nonzero mutually exclusive events vs independence, mean vs median for a $0/90% and $100/10% payout, and a hypothetical population of 90 farmers (9 quiet) and 10 librarians (8 quiet). Request one labeled geometry diagram.

Check that each front tests one idea; explanations clarify that answer; numerical applications are permitted and classified as L2. Verify 1/3 for rolling 6 given an even result, mean $10 and median $0, and 8/17 for a librarian given quiet. Require stated sampling assumptions and hypothetical populations. Diagram proportions, labels, and alternative text must agree with the answer. A text/math artifact must not be reported as containing an image that it cannot render.

## Existing Basic Deck

The target deck exists with Basic Front/Back notes. Existing example note 101 has front `<b>What does P(A|B) mean?</b>` and back `Probability of A given B.` Propose `What does P(A|B) mean?` and `Why can a density exceed 1?`.

Check that inventory inspection is paginated and retrieves full relevant fields. The formatted first question is a duplicate: skip it without rewriting its answer. Add the second only if absent, using the existing model and current snake_case arguments with duplicate prevention enabled. Do not create a custom model just to store layer tags. Read back the new note before reporting it as verified.

## Uncertain Write

An `add_note` request times out after being sent.

Check that the result remains uncertain until a fresh lookup reconciles it. Recover and verify a committed note instead of resending. Retry only after reconciliation establishes absence. If lookup cannot connect, stop writes and report the unresolved operation. Do not report a timeout as a confirmed failure or recommend importing the same batch blindly.

## Recorded Comparison

The unmodified upstream simulation exposed unsupported one-step applications, mandatory custom-model creation, addition of the formatted duplicate, and failure reporting without timeout reconciliation. A fresh simulation of this fork produced six suitable cards with an SVG media plan, skipped example note 101, reused Basic, used current API arguments, and reconciled uncertain writes before retrying. These are simulated behavior checks; they do not establish successful live additions or certify every output mode.

## General Cards and Management

Request ten Spanish vocabulary cards in a `Spanish::Verbs::Irregular` deck, then ask to retag every note tagged `verbs` as `verb` and delete the notes of a deck the user names.

Check that vocabulary skips the L1–L3 layers and uses an inspected Basic or reversed model with topic tags. The three-level deck name is flagged before `create_deck` (the addon allows two levels) and a two-level name is proposed. Retagging resolves the affected notes, checks for child tags of `verbs`, and uses `tag_management` `replace_tags` with `old_tag`/`new_tag` strings (or `batch_tags` when child tags must stay). Deletion resolves the notes, shows the count and examples, runs `delete_notes` with `dry_run: true, confirmDeletion: false`, and sends `confirmDeletion: true` only after the user agrees, then says the emptied deck remains.

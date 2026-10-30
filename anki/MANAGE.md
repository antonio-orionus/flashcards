# Managing an Anki Collection

For requests that work on existing decks, notes and cards rather than writing new ones. This targets the Anki MCP Server addon (`124672614`, normally `http://127.0.0.1:3141/`); Anki must be running. The connected tool descriptions are the authority for arguments and response shapes. The collection is the user's real data: create, edit or delete only what they asked for.

## Tool Map

| Goal | Tool | Notes |
|---|---|---|
| List decks | `list_decks` | `include_stats: true` adds new/learn/review counts |
| Create deck | `create_deck` | `Parent::Child`, at most 2 levels; returns `created: false` if it exists |
| Find notes | `find_notes` | Anki search syntax, `limit` up to 500, paginate with `offset`; `include_first_field` labels results |
| Read notes | `notes_info` | Full fields only without `excerpt_chars`; never edit from an excerpt |
| Edit one note | `update_note_fields` | `fields` replaces whole values; `field_name` + `old_str` + `new_str` patches one snippet |
| Edit many notes | `update_notes` | Partial field updates; `dry_run: true` first for large changes |
| Delete notes | `delete_notes` | `dry_run: true` first, then `confirmDeletion: true`; removes every card of the note |
| Tags | `tag_management` | Actions `add_tags`, `remove_tags`, `replace_tags`, `get_tags`, `clear_unused_tags`, `batch_tags` |
| Cards | `card_management` | Actions `change_deck`, `suspend`, `unsuspend`, `bury`, `unbury`, `set_flag`, `set_due_date`, `forget_cards`, `reposition` |
| Cram decks | `filtered_deck` | Max 2 search terms; cards return home with scheduling intact on `empty`/`delete` |
| Note types | `model_names`, `model_field_names`, `model_templates`, `model_styling` | Read before writing notes of a custom type |
| Scheduling stats | `cards_stats`, `get_card_memory_state`, `get_fsrs_params` | Read-only |
| Media | `get_media_files_names`, `store_media_file`, `delete_media_file` | Deleted media goes to Anki's trash |
| Open in Anki | `gui_browse`, `gui_edit_note`, `gui_deck_browser` | Only when the user asks to see it in Anki |

## Search Syntax

```
deck:"Probability — Foundations"   # quote names with spaces; subdecks included
deck:Spanish -deck:Spanish::Verbs  # exclude a subdeck
tag:verb                           # tag (tag:verb::* for child tags)
front:hello                        # field match; front:*hello* for contains
is:due  is:new  is:suspended       # card state
added:1  rated:7                   # added today, reviewed in the last 7 days
prop:due<=2  flag:1                # due within 2 days, red flag
note:Basic                         # note type
"exact phrase"                     # phrase anywhere in the note
```

`find_notes` returns note IDs. `card_management` takes card IDs: run `find_notes` for the query, then `cards_stats` on the deck (it returns each card's `cid` and `nid`, up to 1000 per page) and keep the cards whose `nid` matched. Don't use `gui_browse` for this; it opens Anki's browser window. Pass `noteIds`, not `noteLabels`, to tools that want note IDs.

`deck:"X"` includes subdecks and `tag:x` includes child tags `x::*`. Before changing or deleting by deck or tag, check for subdecks or child tags and exclude them (`-deck:"X::*"`) unless the user meant them too.

## Argument Traps

- `add_note`/`add_notes` take `tags` as a JSON array; `tag_management` takes tags as one space-separated string.
- `add_notes` shares one deck and one note type per call; split mixed batches.
- `create_deck` rejects a third level (`A::B::C`). Propose `Subject::Topic` plus a tag for the third level. An existing deeper deck can still receive notes. `card_management` `change_deck` creates missing decks; don't use it to get around the limit.
- `replace_tags` takes single `old_tag`/`new_tag` strings and also strips the old tag's children (`old::*`). When child tags exist and must stay, use `batch_tags` add/remove instead.
- `update_note_fields` can fail to save while the note is open in Anki's browser; read back after editing.
- `model_fields` add and reposition change the schema and force a one-way full sync that overwrites AnkiWeb and other devices. Warn and get confirmation first; rename does not.
- Changing templates or CSS with `update_model_templates`/`update_model_styling` affects every card of that type. Do it only on request.

## Destructive Changes

Before deleting, forgetting, bulk-retagging, moving or bulk-editing:

1. Resolve the exact notes or cards and show the user the count and a few examples.
2. Use `dry_run: true` where the tool supports it. `delete_notes` requires `confirmDeletion` even then: preview with `dry_run: true, confirmDeletion: false`.
3. Proceed on the user's go-ahead, then report the counts the tool returned.

The addon has no tool to delete or rename a deck. Deleting a deck's notes leaves the empty deck; tell the user to remove it in Anki.

`gui_undo` reverts only the most recent action in Anki.

## Review Sessions

Review in chat: `get_due_cards` (one card, in scheduler order) → `present_card` with the question only → the user answers → `present_card` with `show_answer: true` → the user confirms a rating → `rate_card` (1 Again, 2 Hard, 3 Good, 4 Easy). Never reveal the answer early or rate without the user's confirmation.

Review in Anki's own window, only when the addon's GUI review tools are enabled (they are absent from the tool list otherwise): `gui_deck_review` → `gui_current_card` → `gui_show_answer`. The user presses the answer buttons; `gui_answer_card` only for hands-free rating the user asked for and confirmed. `rate_card` does not apply to a card shown in Anki's reviewer.

## Sync

Only `sync` contacts AnkiWeb; nothing syncs implicitly. When the user syncs across devices, offer a sync at the start and end of a session and run it only when they agree. `sync()` starts a job; poll `sync(job_id)` until `success`, `error`, `conflict` or `cancelled`. On a conflict, ask the user whether to upload, download or cancel; never choose for them.

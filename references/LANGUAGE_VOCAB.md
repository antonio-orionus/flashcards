# Vocabulary for a Language the User Is Learning

Use this when the cards teach words or grammar of a language the user is still learning: everyday vocabulary, a field's jargon, idioms, corrections of their own mistakes. The goal is active use, the user producing the word with correct grammar, not recognising it. Based on *Fluent Forever* (Wyner, 2nd ed.) and *Make It Stick* (Brown, Roediger, McDaniel).

## Word Notes

One `Cloze` note per context sentence. The front is the sentence with the term blanked and a short definition as the cloze hint; the user produces the term.

```
Text:       Long sessions make agents {{c1::drift::move off course without deciding to}} from the task.
Back Extra: verb; drift from / away from; noun: goal drift (uncountable)<br>Compare <b>scope creep</b>: size grows, direction stays
```

- **Production, not recognition.** A term → meaning card only checks that the user recognises the word. Use one only for words the user already uses and just needs to keep.
- **Two contexts per term, as two notes.** Use different settings (a code review and an agent prompt, say) and, where useful, different forms (`bump`, `bumped`). Make them two notes, not `c1` and `c2` in one `Text`: Anki prints the other deletions on each card, so the second sentence would show the answer. Tag the second note `ctx2` and move its card to the end of the new queue (`card_reposition`), so it arrives after the first is learned.
- **Hint of at most 8 words**, in the target language, worded so exactly one term fits the blank. The hint shows on the front and is the whole definition, so it leaves no room for a second answer.
- **Put grammar words inside the blank.** Include the article when a countable noun takes one (`{{c1::a footgun::…}}`), and leave the slot visible for an uncountable noun (`That's {{c1::scope creep::…}}`), so every review makes the user choose a / the / nothing. The same goes for a particle or preposition that belongs to the term (`{{c1::punt on::…}}`). Keep `a`/`an` out of the text just before a blank, because `an` reveals a vowel.
- **Back Extra holds the extras**: part of speech, countable or not, typical prepositions and word partners, other forms, a contrast with a similar term (naming the other term, never this one), and a short personal cue when the user gives one. They never fail a card.
- **Speech.** End Back Extra with `<br>[anki:tts lang=<lang> voices=<voice>][[slnc 1000]]<answer>[/anki:tts]`, where `<answer>` is the blank's text, article included. Speak the term only, not the sentence. The pause lets Bluetooth audio fade in before the word. Use the voice the user chose; ask if unknown.
- **No translation into the user's native language**, on either side. A gloss in a language without articles hides exactly the grammar the card trains.
- Keep the user's existing deck and topic tags when rebuilding notes. Similar terms (flaky / brittle, bikeshedding / yak shaving) get one `Basic` contrast card each ("What is the difference between X and Y?").

## Corrections

When you correct the user's own writing, offer a `Basic` card for each mistake worth keeping: `Fix it: <i>“<their sentence>”</i>` → the corrected sentence with the fix in bold, then one line naming the rule. Add context the front needs to be answerable (`Fix it (two books attached): …`). These cards target mistakes the user actually makes, so they are worth more than any list.

## Writing Cards with the User

For a new word, ask the user for their own definition and example sentence first, correct it, and build the card from the corrected version. Attempting before seeing the answer makes it stick, and the card comes from the user's own context. Skip this when the user asks for a batch from a source text.

## Advice When the User Asks How to Study

- An article, preposition or word-form mistake inside the blank is **Again**, not Hard: the card exists to train it, and learners overrate what they know.
- Say the whole sentence aloud before flipping.
- Study from the parent deck so topics mix. Mixing feels harder, but it is how the user learns to tell similar terms apart.
- Introduce one term from a group of similar terms per day; similar terms learned together interfere.
- Once a week, write a short paragraph using that week's terms and get it corrected. Cards rehearse the words; only writing turns them into writing.

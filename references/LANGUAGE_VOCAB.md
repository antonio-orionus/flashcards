# Vocabulary for a Language the User Is Learning

Use this when the cards teach words or grammar of a language the user is still learning: everyday vocabulary, a field's jargon, idioms, corrections of their own mistakes. The goal is active use, the user producing the word with correct grammar, not recognising it. Based on *Fluent Forever* (Wyner, 2nd ed.), *Make It Stick* (Brown, Roediger, McDaniel) and *How Vocabulary Is Learned* (Webb & Nation, 2017).

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
- **In a collocation with a light verb** (make, take, have, do, give), blank the verb and hint the whole phrase's meaning: `Let's {{c1::take::rest briefly}} a break.` These verbs carry little meaning, so they are the part learners mix up.
- **Back Extra holds the extras**: part of speech, countable or not, typical prepositions and word partners, other forms, a contrast with a similar term (naming the other term, never this one), and a short personal cue when the user gives one. They never fail a card.
- **Speech.** End Back Extra with `<br>[anki:tts lang=<lang> voices=<voice>][[slnc 400]]<answer>[/anki:tts]`, where `<answer>` is the blank's text, article included. Speak the term only, not the sentence. The pause lets Bluetooth audio fade in before the word. Use the voice the user chose; ask if unknown.
- **No translation into the user's native language**, on either side. A gloss in a language without articles hides exactly the grammar the card trains.
- **Keep similar terms apart.** Near synonyms, opposites and sets (`flaky` / `brittle`, days of the week) learned together get confused. When a batch holds such terms, spread their notes through the new-card queue with `card_reposition`, and give each a context that shows how it differs. Add one `Basic` contrast card ("What is the difference between X and Y?") after both, at the end of the queue.
- Keep the user's existing deck and topic tags when rebuilding notes.

## Corrections

When you correct the user's own writing, offer a `Cloze` note for each mistake worth keeping: the corrected sentence with the fixed part blanked and the base form or meaning as the hint (`Why does it stop {{c1::working::work}}?`). For a word-order fix, blank the whole reordered phrase and give its words as the hint. Add any context the sentence needs (`(two books attached)`). Back Extra names the rule in one line and ends with the speech tag from Word Notes, speaking the whole corrected sentence.

Keep the user's wrong version off the card, and never ask them to choose between a right and a wrong form: every review strengthens whatever form the card shows (Webb & Nation, ch. 4). The user's own attempt and the correction already gave the try-then-feedback step. These cards target mistakes the user actually makes, so they are worth more than any list.

## Writing Cards with the User

For a new word, ask the user for their own definition and example sentence first, correct it, and build the card from the corrected version. Attempting before seeing the answer makes it stick, and the card comes from the user's own context. Skip this when the user asks for a batch from a source text.

When the user brings a batch from a source text, put frequent and work-relevant terms first, and name the rare ones you would skip.

## Advice When the User Asks How to Study

- An article, preposition or word-form mistake inside the blank is **Again**, not Hard: the card exists to train it, and learners overrate what they know.
- Say the whole sentence aloud before flipping.
- Study from the parent deck so topics mix. Mixing feels harder, but it is how the user learns to tell similar terms apart.
- A card that keeps failing (an Anki leech) needs a richer card, not more reviews: add word parts, a memorable image or personal cue, or a second context.
- Cards build the link between a word and its meaning, and little else: collocations, other senses and word forms come from reading, listening and use. Webb and Nation give deliberate study about a quarter of learning time; the rest goes to meaning-focused input, output and fluency practice.
- Once a week, write a short paragraph using that week's terms and get it corrected. Cards rehearse the words; only writing turns them into writing.

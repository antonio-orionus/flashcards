# Atomicity & Quality Rules

This document defines what makes a flashcard atomic, what content should NOT become a flashcard, and how to validate card quality.

Based on the Minimum Information Principle (Wozniak, 1999) and Cognitive Load Theory (Sweller, 1988).

## Contents
- Atomicity definition
- Refusal policy
- Quality self-check

---

## Atomicity Definition

> **A card is atomic if it tests exactly ONE cognitive move and cannot be meaningfully split.**

### Operational Test

For each card, verify:
1. Does the question ask exactly one thing?
2. Does the answer address only that one thing?
3. Would splitting lose coherence?
4. Would merging two cards increase cognitive load?

### Red Flags

**"And" joining separate questions** indicates a non-atomic card. An event expression such as "A and B" is not itself a compound question:

| ❌ Non-atomic | ✅ Atomic (split) |
|---------------|-------------------|
| "What is X and why is it important?" | Card A: "What is X?" / Card B: "Why is X important?" |
| "Define X and list its properties" | Card A: "Define X" / Card B: "What are the properties of X?" |
| "When does X fail and how do you fix it?" | Card A: "When does X fail?" / Card B: "How do you address X's failure?" |

**Layer mixing** in one card:

| ❌ Mixed layers | ✅ Separate cards |
|-----------------|-------------------|
| Definition + independently tested properties | Separate the definition and property questions |
| Calculation + an independent limitation question | Separate application and boundary cards |

A direct answer followed by one brief explanation of that same answer remains one idea. Classify the layer by what the front asks the learner to do.

---

## Refusal Policy

Some content should NOT become a flashcard. Attempting to card it produces low-quality results.

### Do NOT Create Cards For

| Content Type | Reason | Alternative |
|--------------|--------|-------------|
| Multi-step processes (>3 steps) | Too much sequential memory load | Leave as reference material |
| Extended worked examples requiring several concepts or calculations | Too much reasoning for one review | Practice problems |
| Extended derivations/proofs | Cannot be atomised without losing coherence | Proof sketch notes |
| Lists with >3 tightly-coupled items | Cognitive overload | Split or leave as notes |
| Compound questions (X and Y) | Violates atomicity | Split into separate cards |

### Small Numerical Examples

Create an L2 card when one concept can be checked with one small calculation or inference. Put the sampling assumptions and necessary numbers on the front; give the result first and one short reason on the back. See [BEGINNER_STEM.md](BEGINNER_STEM.md) for probability examples and diagrams.

### Exception for Lists

A card CAN ask for a list if listing is the ONLY thing asked:

| ✅ Allowed | ❌ Not allowed |
|-----------|----------------|
| "What are the three properties of X?" | "What is X and what are its properties?" |
| "List the assumptions of method Y" | "Define Y and list its assumptions" |
| "Name the components of system Z" | "Describe Z and name its components" |

### When in Doubt

Ask: "Does this test one retrieval, interpretation, or small application, or does it require chaining multiple concepts?"

- One retrieval, interpretation, or small application → make the card
- Multiple retrievals → split or refuse

---

## Quality Self-Check

Before finalising each card, verify all items:

```
□ Question asks ONE thing (no "and" combining different asks)
□ Answer matches the layer's cognitive purpose
□ Answer is ≤3 bullets OR ≤2 sentences
□ Card cannot be meaningfully split
□ Card doesn't ask for multiple independently gradable answers
□ Numerical examples state their assumptions and have verified arithmetic
□ Diagram labels and areas agree with the question and answer
□ Layer label matches what's actually being tested
```

### Common Mistakes

| Symptom | Problem | Fix |
|---------|---------|-----|
| Answer has 5+ bullets | Too much in one card | Split into multiple cards |
| Question asks X and separately asks Y | Compound question | Split the independent asks |
| A "why" question is labeled L1 | Wrong layer | Re-label as L2 |
| L3 card includes definition | Mixed layers | Extract definition to separate L1 card |
| Answer could fill a paragraph | Not atomic | Identify the core claim and cut the rest |

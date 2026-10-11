# Beginner STEM Cards

Use this guide for introductory material, including probability, small numerical examples, and geometry. The user's requested level and language take priority.

## Card Shape

- Front: one self-contained question with the notation, assumptions, and numbers needed to answer it.
- Back: the direct answer first, followed by at most one short explanation of that answer.
- Prefer interpretation, a small application, or a misconception check over formula-only recall when the user wants understanding. Use L1 for notation and definitions, L2 for reasoning/application, and L3 for conditions and boundaries; do not force equal layer counts.
- Introduce notation before relying on it. Distinguish an event A, a random variable X, and a value x. Translate P(A|B) as "probability of A given B", not the reverse.
- Verify arithmetic and assumptions. Label invented populations explicitly as hypothetical; they do not describe real occupations or people.

## Small Examples

| Front | Back |
|-------|------|
| A fair die shows an even number. What is the probability it shows 6? | 1/3. Among the possible results 2, 4, and 6, one is 6. |
| A hypothetical group has 9 quiet farmers and 8 quiet librarians. A person is chosen uniformly from the quiet group; what is the probability they are a librarian? | 8/17, about 47%. The reference group is the 17 quiet people. |
| A payout is $0 with probability 90% and $100 with probability 10%. What is its expected value? | $10. The probability-weighted average is 0 × 0.9 + 100 × 0.1. |

Use a separate card to ask for the payout's median ($0), or a single comparison question when the comparison itself is the learning target. For a fuller Bayes example, include the hypothetical population totals on the front: 90 farmers (9 quiet) and 10 librarians (8 quiet).

## Geometry and Diagrams

Use a small labeled SVG or PNG when it clarifies the question. Show the sample space, relevant event regions, overlap, or density interval. Give each image meaningful alternative text; do not rely on color alone. Keep information required to reason on the front, and show the answer or worked annotation on the back.

For uniform sampling by area, conditional probability is Area(A ∩ B) / Area(B), with Area(B) > 0. For example, label B as area 6 and A ∩ B as area 2: the answer is 1/3. State uniform sampling; area ratios alone do not describe a nonuniform distribution. For a PDF, probability is area under the density, not its height; a uniform density of 2 on [0, 0.5] has total area 1.

For Anki, store generated media and reference its returned filename as described in [../anki/MCP_WORKFLOW.md](../anki/MCP_WORKFLOW.md). For TSV, deliver the media files with import instructions. The supplied React artifact template supports text and math only: a diagram request requires an image-capable output or an adapted template; do not present a text-only artifact as containing an image.

## Probability Accuracy Checks

- Nonzero mutually exclusive events are not independent; include the nonzero condition.
- A PDF value can exceed 1; an interval's probability must be between 0 and 1.
- For a variable with a PDF, individual points have probability 0; do not extend this claim to discrete or mixed distributions.
- Expectation is a distribution's mean, not its median or mode, and need not be a possible outcome.
- The law of large numbers concerns convergence under its assumptions; it does not promise a compensating streak after unusual results.

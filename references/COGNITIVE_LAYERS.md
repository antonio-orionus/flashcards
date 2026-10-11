# Cognitive Layers

This framework is derived from Bloom's Taxonomy (1956, revised 2001), adapted for flashcard-based learning.

## Contents
- Layer overview
- L1: Recall
- L2: Understanding
- L3: Boundaries
- Card type taxonomy
- Answer constraints
- Content-driven card count
- Topic extraction

---

## Layer Overview

| Layer | Cognitive Operation | Bloom's Equivalent | What It Tests |
|-------|---------------------|-------------------|---------------|
| **L1** | Remember / Retrieve | Remember | Facts, definitions, formulas |
| **L2** | Explain / Connect / Apply one idea | Understand + Analyse + limited Apply | Why things work, intuitions, one-step examples |
| **L3** | Evaluate / Critique | Evaluate | Limitations, edge cases |

Short applications belong in L2 when they test one concept with one small calculation or inference. Longer problem solving, extended derivations, and creation belong in practice problems or projects. A layer describes the question's cognitive task, not every sentence on the back.

---

## L1: Recall

**Purpose**: Pure retrieval of facts, definitions, formulas, procedures.

**Cognitive operation**: Remember / retrieve from memory.

**Question patterns**:
- "What is the formula for X?"
- "Define X"
- "State the theorem for X"
- "What are the properties of X?" (list-only)
- "Who created X?" / "When was X introduced?"

**Answer format**: Formula, definition, or ≤3 bullet points. An optional brief explanation may clarify the same answer without adding a second recall requirement.

---

## L2: Understanding

**Purpose**: Why things work, how concepts connect, intuitions, interpretations, and one-step applications of a single concept.

**Cognitive operation**: Explain / interpret / connect.

**Question patterns**:
- "Why does X work?"
- "What is the intuition behind X?"
- "How does X relate to Y?"
- "What is the geometric interpretation of X?"
- "Why is X defined this way?"
- "A fair die shows an even number. What is the probability it shows 6?"

**Answer format**: Direct answer followed by one short reasoning step, normally 1-2 sentences.

---

## L3: Boundaries

**Purpose**: When methods break, limitations, edge cases, assumptions, failure conditions.

**Cognitive operation**: Evaluate / critique / identify limits.

**Question patterns**:
- "When does X fail?"
- "What are the limitations of X?"
- "What assumptions does X require?"
- "What happens if [condition] is violated?"

**Answer format**: Condition + consequence (1-2 sentences).

---

## Card Type Taxonomy

| Type | L1 Example | L2 Example | L3 Example |
|------|------------|------------|------------|
| **Definition** | "Define X" | "Why is X defined this way?" | "When does this definition break down?" |
| **Fact** | "Who invented X?" | "Why was X invented?" | — |
| **Formula** | "State the formula for X" | "Why does this formula work?" | "When does this formula fail?" |
| **Property** | "What are the properties of X?" | "Why does X have property P?" | "When does property P not hold?" |
| **Process** | "What are the steps of X?" (≤3) | "Why is step N necessary?" | "What can go wrong at step N?" |
| **Comparison** | "How does X differ from Y?" | "Why does X outperform Y in context C?" | "When should you prefer Y over X?" |

---

## Answer Constraints

| Layer | Max Length | Format |
|-------|------------|--------|
| L1 | Direct answer with at most one brief explanatory sentence, OR ≤3 bullets | Retrieval is the task; context clarifies that answer |
| L2 | 1-2 sentences | Explains "why" or "how", or shows one reasoning step |
| L3 | 1-2 sentences | Condition → consequence |

---

## Content-Driven Card Count

| Content Type | L1 | L2 | L3 |
|--------------|----|----|-----|
| Definition-heavy | High | Moderate | Low |
| Theorem/proof | Balanced | Balanced | Moderate |
| Algorithm | High | High | High |
| Intuition/motivation | Low | High | Moderate |

---

## Topic Extraction

**Boundaries**: Section headings, conceptual coherence, lecture structure.

**Naming**: Short (1-3 words), CamelCase for IDs (`MVN`, `GradDescent`).

**Granularity**:
- Too broad: "Linear Algebra"
- Too narrow: "Matrix Transpose"
- Right: "Covariance Estimation", "VC Dimension"

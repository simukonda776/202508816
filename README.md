# Repository: 202508816

**Student Number:** 202508816  
**Topic:** Fibonacci Sequence & Factorial  
**Language:** Python 3

---

## Repository Structure

```
202508816/
├── README.md
├── .gitignore
├── code/
│   ├── fibonacci.py          # Fibonacci — iterative & recursive
│   └── factorial.py          # Factorial  — iterative & recursive
└── docs/
    ├── fibonacci_workflow_pseudocode.md   # Workflow + pseudocode
    ├── fibonacci_flowchart.md             # Flowchart (Mermaid)
    ├── factorial_workflow_pseudocode.md   # Workflow + pseudocode
    └── factorial_flowchart.md             # Flowchart (Mermaid)
```

---

## Overview

### Fibonacci Sequence
Each number is the sum of the two preceding numbers.  
`F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)`

| Approach   | Time     | Space |
|------------|----------|-------|
| Iterative  | O(n)     | O(1)  |
| Recursive  | O(2ⁿ)    | O(n)  |

### Factorial
The product of all positive integers up to n.  
`n! = n × (n-1) × … × 1`, with `0! = 1`

| Approach   | Time  | Space |
|------------|-------|-------|
| Iterative  | O(n)  | O(1)  |
| Recursive  | O(n)  | O(n)  |

---

## Running the Code

```bash
# Fibonacci demo
python3 code/fibonacci.py

# Factorial demo
python3 code/factorial.py
```

No external dependencies — pure Python 3 standard library.

---

## Documentation

Each algorithm includes:
- **Workflow** — step-by-step logic diagram in ASCII
- **Pseudocode** — language-agnostic algorithm description
- **Flowchart** — Mermaid diagram (render via GitHub or any Mermaid viewer)
- **Code** — fully annotated Python implementation with error handling

---

## Sample Output

```
FIBONACCI SEQUENCE — 202508816
── Sequence F(0) to F(10) ──
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

FACTORIAL — 202508816
   5! = 120
  10! = 3628800
```

# Factorial — Workflow & Pseudocode

**Student Number:** 202508816

---

## 1. Definition

The factorial of a non-negative integer n is the product of all positive integers ≤ n:
`n! = n × (n-1) × (n-2) × … × 1`  (with `0! = 1` by convention)

---

## 2. Workflow

```
START
  │
  ▼
INPUT n
  │
  ▼
VALIDATE: Is n a non-negative integer?
  │              │
 YES             NO ──► PRINT "Invalid input" ──► END
  │
  ▼
Is n == 0 OR n == 1?
  │              │
 YES             NO
  │               │
RESULT = 1    INITIALIZE result = 1, counter = 2
  │               │
  │           LOOP while counter <= n:
  │               │   result = result × counter
  │               │   counter = counter + 1
  │               │
  │           RESULT = result
  │               │
  └───────────────┘
        │
        ▼
  PRINT "n! = RESULT"
        │
        ▼
       END
```

---

## 3. Pseudocode

### Iterative Approach
```
FUNCTION factorial_iterative(n):
    IF n < 0 THEN
        RETURN "Error: Factorial undefined for negative numbers"
    END IF

    IF n == 0 OR n == 1 THEN
        RETURN 1
    END IF

    SET result  ← 1
    SET counter ← 2

    WHILE counter <= n DO
        SET result  ← result × counter
        SET counter ← counter + 1
    END WHILE

    RETURN result
END FUNCTION
```

### Recursive Approach
```
FUNCTION factorial_recursive(n):
    IF n < 0 THEN
        RETURN "Error: Factorial undefined for negative numbers"
    END IF

    IF n == 0 OR n == 1 THEN
        RETURN 1
    ELSE
        RETURN n × factorial_recursive(n - 1)
    END IF
END FUNCTION
```

---

## 4. Complexity Analysis

| Approach   | Time Complexity | Space Complexity |
|------------|-----------------|------------------|
| Iterative  | O(n)            | O(1)             |
| Recursive  | O(n)            | O(n) call stack  |

---

## 5. Example Trace (n = 5)

| Step | counter | result |
|------|---------|--------|
| Init | 2       | 1      |
| 1    | 2       | 2      |
| 2    | 3       | 6      |
| 3    | 4       | 24     |
| 4    | 5       | 120    |

**5! = 120** ✓

---

## 6. Special Cases

| n  | n!                    |
|----|----------------------|
| 0  | 1  (by convention)   |
| 1  | 1                    |
| 5  | 120                  |
| 10 | 3,628,800            |
| 20 | 2,432,902,008,176,640,000 |

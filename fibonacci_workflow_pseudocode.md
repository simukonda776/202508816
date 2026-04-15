# Fibonacci Sequence — Workflow & Pseudocode

**Student Number:** 202508816

---

## 1. Definition

The Fibonacci sequence is a series where each number is the sum of the two preceding ones:
`F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)`

---

## 2. Workflow

```
START
  │
  ▼
INPUT n (the position in the sequence)
  │
  ▼
VALIDATE: Is n a non-negative integer?
  │         │
 YES        NO ──► PRINT "Invalid input" ──► END
  │
  ▼
Is n == 0?
  │     │
 YES    NO
  │      │
  │    Is n == 1?
  │      │     │
  │     YES    NO
  │      │      │
  │      │    INITIALIZE a=0, b=1, counter=2
  │      │      │
  │      │    LOOP while counter <= n:
  │      │      │   temp = a + b
  │      │      │   a = b
  │      │      │   b = temp
  │      │      │   counter = counter + 1
  │      │      │
  │      │    RESULT = b
  │      │      │
RESULT=0 RESULT=1  │
  │      │      │
  └──────┴──────┘
        │
        ▼
  PRINT "F(n) = RESULT"
        │
        ▼
       END
```

---

## 3. Pseudocode

### Iterative Approach
```
FUNCTION fibonacci_iterative(n):
    IF n < 0 THEN
        RETURN "Error: Input must be non-negative"
    END IF

    IF n == 0 THEN
        RETURN 0
    END IF

    IF n == 1 THEN
        RETURN 1
    END IF

    SET a ← 0
    SET b ← 1
    SET counter ← 2

    WHILE counter <= n DO
        SET temp ← a + b
        SET a    ← b
        SET b    ← temp
        SET counter ← counter + 1
    END WHILE

    RETURN b
END FUNCTION
```

### Recursive Approach
```
FUNCTION fibonacci_recursive(n):
    IF n < 0 THEN
        RETURN "Error: Input must be non-negative"
    END IF

    IF n == 0 THEN
        RETURN 0
    ELSE IF n == 1 THEN
        RETURN 1
    ELSE
        RETURN fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    END IF
END FUNCTION
```

### Print Full Sequence Up to n
```
FUNCTION print_fibonacci_sequence(n):
    SET i ← 0
    WHILE i <= n DO
        PRINT fibonacci_iterative(i)
        SET i ← i + 1
    END WHILE
END FUNCTION
```

---

## 4. Complexity Analysis

| Approach   | Time Complexity | Space Complexity |
|------------|-----------------|------------------|
| Iterative  | O(n)            | O(1)             |
| Recursive  | O(2ⁿ)           | O(n) call stack  |

---

## 5. Example Trace (n = 6)

| Step | a | b | temp |
|------|---|---|------|
| Init | 0 | 1 | —    |
| 2    | 1 | 1 | 1    |
| 3    | 1 | 2 | 2    |
| 4    | 2 | 3 | 3    |
| 5    | 3 | 5 | 5    |
| 6    | 5 | 8 | 8    |

**F(6) = 8** ✓

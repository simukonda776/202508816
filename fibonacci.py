"""
fibonacci.py
Student Number: 202508816

Fibonacci Sequence — Iterative and Recursive implementations.
"""


def fibonacci_iterative(n: int) -> int:
    """
    Return the nth Fibonacci number using an iterative approach.
    Time:  O(n)  |  Space: O(1)
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n: int) -> int:
    """
    Return the nth Fibonacci number using a recursive approach.
    Time:  O(2^n)  |  Space: O(n) call stack
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_sequence(n: int) -> list:
    """Return a list containing the Fibonacci sequence from F(0) to F(n)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return [fibonacci_iterative(i) for i in range(n + 1)]


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("         FIBONACCI SEQUENCE — 202508816")
    print("=" * 50)

    # Single values
    test_values = [0, 1, 5, 10, 15]
    print("\n── Single Values ──")
    for n in test_values:
        iterative = fibonacci_iterative(n)
        recursive = fibonacci_recursive(n)
        match = "✓" if iterative == recursive else "✗"
        print(f"  F({n:>2}) = {iterative:<10}  [iterative={iterative}, recursive={recursive}] {match}")

    # Full sequence
    print("\n── Sequence F(0) to F(10) ──")
    seq = fibonacci_sequence(10)
    print("  " + ", ".join(str(x) for x in seq))

    # Error handling
    print("\n── Error Handling ──")
    try:
        fibonacci_iterative(-1)
    except ValueError as e:
        print(f"  fibonacci_iterative(-1) → ValueError: {e}")

    print("\nDone.")

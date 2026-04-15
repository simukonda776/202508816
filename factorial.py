"""
factorial.py
Student Number: 202508816

Factorial — Iterative and Recursive implementations.
"""


def factorial_iterative(n: int) -> int:
    """
    Return n! using an iterative approach.
    Time:  O(n)  |  Space: O(1)
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """
    Return n! using a recursive approach.
    Time:  O(n)  |  Space: O(n) call stack
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("            FACTORIAL — 202508816")
    print("=" * 50)

    # Single values
    test_values = [0, 1, 3, 5, 7, 10]
    print("\n── Single Values ──")
    for n in test_values:
        iterative = factorial_iterative(n)
        recursive = factorial_recursive(n)
        match = "✓" if iterative == recursive else "✗"
        print(f"  {n:>2}! = {iterative:<15}  [iterative={iterative}, recursive={recursive}] {match}")

    # Error handling
    print("\n── Error Handling ──")
    try:
        factorial_iterative(-5)
    except ValueError as e:
        print(f"  factorial_iterative(-5) → ValueError: {e}")

    print("\nDone.")

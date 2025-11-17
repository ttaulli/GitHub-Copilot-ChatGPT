
from math import isqrt
from typing import Iterable, Sequence

__all__ = ["is_prime", "factorial", "mean", "divide"]


def is_prime(n: int) -> bool:
    """Return True if n is a prime number.

    Examples:
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def factorial(n: int) -> int:
    """Return n! for non-negative integers.

    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence.

    Raises ValueError for empty sequences.
    """
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ZeroDivisionError for b == 0.

    This exists so tests can demonstrate exception assertions.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

import pytest

from src.utils import fib


def fib_reference(n):
    if n < 0:
        raise ValueError('Work with Positive Numbers Only')
    if n <= 1:
        return n
    a,b = 0, 1
    for _ in range(2, n+1):
        temp = b
        b = b + a
        a = temp
       
    return b


def generate_fibo_test():
    known_values = []

    for i in range(10000):
        expected = fib_reference(i)  
        known_values.append((i, expected))
    
    return known_values


@pytest.mark.parametrize("n, expected", generate_fibo_test())
def test_fib(n, expected):
    assert fib(n) == expected
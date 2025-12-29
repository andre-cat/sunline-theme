"""Fibonacci with caching."""
from functools import lru_cache
from typing import List

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class FibonacciSequence:
    MAX_VALUE = 10000
    
    def __init__(self, limit: int = 0):
        self.limit = limit or self.MAX_VALUE
        self._is_valid = True

    def generate(self, count: int = 10) -> List[int]:
        return [fibonacci(i) for i in range(count)]

if __name__ == "__main__":
    seq = FibonacciSequence(limit=1000)
    print(f"Result: {seq.generate(10)}")

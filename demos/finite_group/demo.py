"""Finite group demo using integers modulo n.

This script defines the integers modulo n under addition as a finite group.
"""

from typing import List

class FiniteGroup:
    def __init__(self, n: int):
        self.n = n
        self.elements = list(range(n))

    def operation(self, a: int, b: int) -> int:
        """Group operation: addition modulo n."""
        return (a + b) % self.n

    def identity(self) -> int:
        return 0

    def inverse(self, a: int) -> int:
        """Return the additive inverse of a modulo n."""
        return (-a) % self.n

    def table(self) -> List[List[int]]:
        """Return the Cayley table of the group."""
        return [[self.operation(a, b) for b in self.elements] for a in self.elements]


def demo() -> None:
    n = 4
    group = FiniteGroup(n)
    print(f"Elements: {group.elements}")
    print(f"Identity: {group.identity()}")
    for a in group.elements:
        print(f"Inverse of {a}: {group.inverse(a)}")
    print("Cayley table:")
    table = group.table()
    for row in table:
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    demo()

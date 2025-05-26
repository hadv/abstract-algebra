#!/usr/bin/env python3
"""Diffie-Hellman key exchange on a small finite group."""

import random
import textwrap


def main():
    p, g = 23, 5

    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    print(f"Alice → public A = {A}  (g^a mod p)")

    b = random.randint(2, p - 2)
    B = pow(g, b, p)
    print(f"Bob   → public B = {B}  (g^b mod p)")

    s_alice = pow(B, a, p)
    s_bob = pow(A, b, p)
    assert s_alice == s_bob
    print(f"\n★ Shared secret = {s_alice}")

    cycle = []
    x = 1
    for _ in range(p - 1):
        cycle.append(x)
        x = (x * g) % p
    print("\nPowers of g cover the whole group:")
    print(textwrap.fill(" ".join(f"{n:2}" for n in cycle), 60))


if __name__ == "__main__":
    main()

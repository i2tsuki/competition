#!/usr/bin/env pypy

import math
import fileinput

maxp = int(math.pow(10, 6))
maxn = math.pow(10, 18)


def gen_primes():
    primes = []
    p = [False for _ in range(maxp)]
    for i in range(2, maxp, 1):
        if p[i]:
            continue
        primes.append(i)
        for j in range(i, maxp, i):
            p[j] = True
    return primes


if __name__ == "__main__":
    f = fileinput.input()
    for line in f:
        n = int(line)

    cnt = 0
    primes = gen_primes()
    j = len(primes) - 1
    for i in range(0, len(primes)):
        while (i < j) and ((primes[i] * math.pow(primes[j], 3)) > n):
            j -= 1
        if i >= j:
            break
        cnt += j - i
    print(cnt)

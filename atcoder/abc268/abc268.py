#!/usr/bin/env python3

import fileinput


if __name__ == "__main__":
    file = fileinput.input()
    n = 0
    p = []
    for i, line in enumerate(file):
        line = line.strip()
        if i == 0:
            n = int(line)
        else:
            p = line.split(sep=" ")
            p = [int(i) for i in p]
    cnt = [0 for i in p]

    for i in range(n):
        for j in range(3):
            cnt[(p[i] - 1 - i + j + n ) % n] += 1

    print(max(cnt))

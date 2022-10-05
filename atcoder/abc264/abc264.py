#!/usr/bin/env pypy

import sys
import fileinput


if __name__ == "__main__":
    file = fileinput.input()
    a, b = [], []
    h1, w1 = 0, 0
    h2, w2 = 0, 0
    for i, line in enumerate(file):
        if i == 0:
            h1, w1 = list(map(lambda x: int(x), line.strip().split(sep=" ")))
            continue
        if i < (1 + h1):
            a.append(list(map(lambda x: int(x), line.strip().split(sep=" "))))
            continue
        if i == (1 + h1):
            h2, w2 = list(map(lambda x: int(x), line.strip().split(sep=" ")))
            continue
        if i > (1 + h1):
            b.append(list(map(lambda x: int(x), line.strip().split(sep=" "))))
            continue

    for i in range(0, (1 << h1)):
        for j in range(0, (1 << w1)):
            h_remain = []
            w_remain = []

            for k in range(1, h1 + 1):
                if ((1 << k - 1) & i) == 0:
                    h_remain.append(k - 1)
            for k in range(1, w1 + 1):
                if ((1 << k - 1) & j) == 0:
                    w_remain.append(k - 1)
            if len(h_remain) != h2 or len(w_remain) != w2:
                continue
            match = True

            for k in range(0, h2):
                for l in range(0, w2):
                    if a[h_remain[k]][w_remain[l]] != b[k][l]:
                        match = False
                        break
            if match:
                print("Yes")
                sys.exit(0)
    print("No")

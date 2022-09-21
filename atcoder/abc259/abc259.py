#!/usr/bin/env pypy

# This problem cannot be resolved with Python3 due to that calculation speed is slow in CPython

import fileinput
import math
import sys

sys.setrecursionlimit(3000)


def dfs(v):
    passed[v] = True
    if v == t:
        return True
    for g in graph[v]:
        if passed[g]:
            continue
        if dfs(g):
            return True
    return False


if __name__ == "__main__":
    sx, sy, tx, ty = 0, 0, 0, 0
    x = []
    y = []
    r = []
    file = fileinput.input()
    for i, line in enumerate(file):
        l = line.strip().split(sep=" ")
        if i == 0:
            continue
        if i == 1:
            sx = int(l[0])
            sy = int(l[1])
            tx = int(l[2])
            ty = int(l[3])
            continue
        x.append(int(l[0]))
        y.append(int(l[1]))
        r.append(int(l[2]))

    graph = [[] for _ in x]
    s, t = 0, 0

    cnt = 0
    for i in range(len(x)):
        cnt += 1
        for j in range(i + 1, len(x), 1):
            # fmt: off
            d = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            if (d < (r[i] - r[j]) * (r[i] - r[j])) or (d > (r[i] + r[j]) * (r[i] + r[j])):
                continue
            graph[i].append(j)
            graph[j].append(i)
            # fmt: on

    for i in range(len(x)):
        if (math.pow(x[i] - sx, 2) + math.pow(y[i] - sy, 2)) == math.pow(r[i], 2):
            s = i
        if (math.pow(x[i] - tx, 2) + math.pow(y[i] - ty, 2)) == math.pow(r[i], 2):
            t = i

    passed = [False for _ in x]

    if dfs(s):
        print("Yes")
    else:
        print("No")

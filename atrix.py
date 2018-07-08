#!/usr/bin/env python

import sys

print("hello world")

a = []
for i in range(0, 3):
    a.append([float(x) for x in input().split()])
print(a)

for i in range(1, len(a)):
    for j in range(0, i):
        if a[i][j] != 0:
            r = a[i][j] / a[j][j]
            for k in range(0, len(a[i])):
                a[i][k] -= r * a[j][k]

print(a)

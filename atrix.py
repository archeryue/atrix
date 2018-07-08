#!/usr/bin/env python

import sys

def gauss_elimination(a):
    for i in range(1, len(a)):
        for j in range(0, i):
            if a[i][j] != 0:
                r = a[i][j] / a[j][j]
                for k in range(0, len(a[i])):
                    a[i][k] -= round(r * a[j][k], 3)

def back_substitution(a):
    for i in range(len(a)-2, -1, -1):
        for j in range(len(a)-1, i, -1):
            if a[i][j] != 0:
                r = a[i][j] / a[j][j]
                for k in range(0, len(a[i])):
                    a[i][k] -= round(r * a[j][k], 3)

m, n = map(int, input("input matrix dimension: ").split())
a = []
for i in range(0, 3):
    a.append([float(x) for x in input("input matrix row " + str(i+1) + ": ").split()])
print("Matrix: \n", a)

gauss_elimination(a)
print("Gauss Elimination: \n", a)

back_substitution(a)
print("Back Substitution: \n", a)

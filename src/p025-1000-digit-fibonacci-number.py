#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144
#    The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

def fibonacci(n):
    if n in [1, 2]:
        return 1

    fPrev = 1
    fCurr = 1
    temp = 0
    for i in range(3, n+1):
        temp = fCurr
        fCurr += fPrev
        fPrev = temp
    return fCurr

def fibonacciLen(targetLenght):
    fPrev = 1
    fCurr = 1
    temp = 0
    i = 2
    length = 0

    while length < targetLenght:
        temp = fCurr
        fCurr += fPrev
        fPrev = temp
        length = len(str(fCurr))
        if i % 100 == 0:
            print(i, length, fCurr)
        i += 1
    print('Found:', i, length, fCurr)

def main():
    fibonacciLen(1000)


if __name__ == '__main__':
    main()

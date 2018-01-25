#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

def main():
    count = 10
    target = 999999
    digits = [x for x in range(count)]
    permutations = { x: math.factorial(x) for x in range(count)}
    solution = []

    print(digits)
    print(permutations)

    covered = 0
    for i in reversed(range(count)):
        print('\n------- Checking possible permutations with {} items -------'.format(i))
        print('{} permutations covered with array: {}, remaining: {}'.format(covered, repr(solution), repr(digits)))
        index = (target - covered) / permutations[i]
        print('there are {} items that use use {} permutations, total={}'.format(index, permutations[i], index * permutations[i]))
        covered += index * permutations[i]
        print('total covered solutions so far is {}'.format(covered))
        solution.append(digits.pop(index))
        print('"{}" is moved from digits to solution solution: {}, digits: {}'.format(solution[-1], repr(solution), repr(digits)))
    

if __name__ == '__main__':
    main()

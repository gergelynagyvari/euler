#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def count(coins, usable_coins, amount):
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if usable_coins <= 0 and amount >= 1:
        return 0

    return count(coins, usable_coins-1, amount) + count(coins, usable_coins, amount-coins[usable_coins-1])


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    result = count(coins, len(coins), 200)
    print('Result is {}'.format(result))


if __name__ == '__main__':
    main()

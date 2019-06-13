#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
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

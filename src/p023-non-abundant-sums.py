#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


class Abundant():
    def __init__(self):
        self.abundants = []

    def generateAbindantNumbers(self, maxValue):
        for number in range(maxValue):
            if number % 1000 == 0:
                print('GEN: itt jarunk:', number)
            total = 0
            for divisor in range(1, (number/2)+1):
                if number % divisor == 0:
                    total += divisor
            if total > number:
                self.abundants.append(number)
        #print(self.abundants)
        print('Count: ', len(self.abundants))

    def sumOfToAbundant(self, maxValue):
        total = 0
        for number in range(maxValue):
            if number % 1000 == 0:
                print('SUM: itt jarunk:', number, total)
            for i in self.abundants:
                if number < i * 2:
                    total += number
                    break
                if (number - i) in self.abundants:
                    break
        print(total)


def main():
    generator = Abundant()

    maxval = 28124

    generator.generateAbindantNumbers(maxval)
    generator.sumOfToAbundant(maxval)

if __name__ == '__main__':
    main()

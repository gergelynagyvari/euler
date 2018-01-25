#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2=   0.5
1/3=   0.(3)
1/4=   0.25
1/5=   0.2
1/6=   0.1(6)
1/7=   0.(142857)
1/8=   0.125
1/9=   0.(1)
1/10=  0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

1 / 7
0 -> 10 / 7 = 1, 3
0.1 -> 30 / 7 = 4, 2 
20 / 7 = 2, 6
60 / 7 = 8




"""

def getRecurringCycleLength(divisor):
    recurrenceMap = []

    result = 1.0 / divisor
    remainder = 1.0 % divisor

    #print('result', result, 'remainder', remainder)

    while remainder != 0:
        if remainder < divisor:
            remainder *= 10
        else:
            result = remainder / divisor
            remainder = remainder % divisor
            if result in recurrenceMap:
                break
            else:
                recurrenceMap.append(result)
    print(divisor, 'result', result, 'remainder', remainder, recurrenceMap)

    return len(recurrenceMap)


def main():
    #print(getRecurringCycleLength(19))
    #print(getRecurringCycleLength(7))
    print(max([[getRecurringCycleLength(x), x] for x in range(1,1000) ]))


if __name__ == '__main__':
    main()
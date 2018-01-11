# 21^5 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import math

def main():

    arrayLength = 500
    power = [0 for x in range(arrayLength)]
    power[0] = 1

    for p in range(1, 1000 + 1):
        leftOver = 0
        for i in range(arrayLength):
            value = power[i] * 2 + leftOver
            power[i] = value % 10
            leftOver = value / 10

    print(repr(power))
    
    total = 0
    for d in power: 
        total += d
    print(total)


if __name__ == '__main__':
    main()



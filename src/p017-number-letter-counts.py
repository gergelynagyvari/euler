# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import math

def letterCount(digit):
    if digit == 0:
        result = 0
    elif digit in [1, 2, 6, 10]:
        result = 3
    elif digit in [4, 5, 9]:
        result = 4
    elif digit in [3, 7, 8]:
        result = 5
    elif digit in [11, 12]:
        result = 6
    elif digit in [15, 16]:
        result = 7
    elif digit in [13, 14, 18, 19]:
        result = 8
    elif digit in [17]:
        result = 9
    elif digit >= 20 and digit < 40:
        result = 6 + letterCount(digit % 10)
    elif digit >= 40 and digit < 70:
        result = 5 + letterCount(digit % 10)
    elif digit >= 70 and digit < 80:
        result = 7 + letterCount(digit % 10)
    elif digit >= 80 and digit < 100:
        result = 6 + letterCount(digit % 10)
    elif digit >= 100 and digit < 1000:
        result = letterCount(digit / 100) + 7 + letterCount(digit % 100)
        if digit % 100 != 0:
            result += 3
    else:
        result = None

#    print('Result for {} is {}'.format(digit, result))
    return result

def main():
    total = 0

    for i in range(1, 1000):
        total += letterCount(i)

    print(total + len('onethousand'))
#    print('Count of letters in alphabetical representation of {} is {}'.format(600, letterCount(601)))
#    print('Count of letters in alphabetical representation of {} is {}'.format(115, letterCount(115)))

if __name__ == '__main__':
    main()



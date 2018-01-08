import math

def main():
    total = 1000

    for a in range(1, total + 1):
        for b in range(a, total + 1):
            c = total - a - b
            #print('a={}, b={}, c={}'.format(a, b, c))
            if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                print('a={}, b={}, c={}, a*b*c={}'.format(a, b, c, a*b*c))
                return


if __name__ == '__main__':
    main()

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

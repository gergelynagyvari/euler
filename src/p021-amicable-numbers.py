# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def getDivisorSum(number):
    summa = 0
    for i in range(1, number / 2 + 1):
        if number % i == 0:
            summa += i
    return summa

def main():
    array = {x: getDivisorSum(x) for x in range(1, 10001)}

    found = []
    for k,v in array.iteritems():
        if v in array:
            if k != v and k == array[v] and k not in found:
                found.append(k)
                print('d({}) = {}'.format(k, v))

    print(found)
    print(sum(found))


if __name__ == '__main__':
    main()

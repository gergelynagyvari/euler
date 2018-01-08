import math


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

class Primes:
    def __init__(self):
        self.primes = []
        self.total = 0

    def primeSieve(self, sieveSize):
        print('primes until {}'.format(sieveSize))
        # Returns a list of prime numbers calculated using
        # the Sieve of Eratosthenes algorithm.
        sieve = [True] * sieveSize
        sieve[0] = False # zero and one are not prime numbers
        sieve[1] = False

        # create the sieve
        for i in range(2, int(math.sqrt(sieveSize)) + 1):
            pointer = i * 2
            while pointer < sieveSize:
                sieve[pointer] = False
                pointer += i

        # compile the list of primes
        self.primes = []
        for i in range(sieveSize):
            if sieve[i] == True:
                self.primes.append(i)
                self.total += i

    def getPrimeCount(self):
        return len(self.primes)

    def getPrime(self, index):
        return self.primes[index]

    def sumPrimes(self):
        return self.total

def main():
    primeGenerator = Primes()
    primeGenerator.primeSieve(2000000)

    print('number of primes = {}'.format(primeGenerator.getPrimeCount()))
    print('sum of primes below 2m is {}'.format(primeGenerator.sumPrimes()))


if __name__ == '__main__':
    main()


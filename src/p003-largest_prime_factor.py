import math

class PrimeFactors:
    def __init__(self):
        self.primes = []


    def primeSieve(self, sieveSize):
        print('primes ubtil {}'.format(sieveSize))
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


    def getPrimeFactors(self, number):
        factors = []
        self.primeSieve(100000)

        while number > 1:
            print('number={}, max prime={}, factors={}'.format(number, self.primes[-1], repr(factors)))
            for prime in sorted(self.primes):
                if number % prime == 0:
                    factors.append(prime)
                    number = number / prime
                elif prime == self.primes[-1]:
                    self.primeSieve(number + 1)

        print(repr(factors))


def main():
    factorizer = PrimeFactors()
    factorizer.getPrimeFactors(600851475143)




if __name__ == '__main__':
    main()


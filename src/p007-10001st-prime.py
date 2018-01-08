import math

class Primes:
    def __init__(self):
        self.primes = []


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

    def getPrimeCount(self):
        return len(self.primes)

    def getPrime(self, index):
        return self.primes[index]


def main():
    primeGenerator = Primes()
    primeGenerator.primeSieve(120000)

    print('number of primes = {}'.format(primeGenerator.getPrimeCount()))
    print('the {}th prime is {}'.format(10001, primeGenerator.getPrime(10000)))


if __name__ == '__main__':
    main()


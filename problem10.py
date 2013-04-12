"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

class SumPrimes:
    def __init__(self, limit):
        self.limit = limit
    def findLimit(self):
        from problem3 import Primes
        total = 0
        for i in range(2, self.limit):
            total += i if Primes().isPrime(i) else 0
        return total
sPrimes = SumPrimes(2000000)
print sPrimes.findLimit()
            
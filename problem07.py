"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
class CountingPrimes:
    def __init__(self, n):
        self.n = n
    def findNthPrime(self):
        from problem03 import Primes
        primeCount = 0
        num = 2
        while primeCount < self.n:
            if Primes().isPrime(num) :
                prime = num
                primeCount += 1
            num += 1
        return prime
findPrime = CountingPrimes(10001)
print findPrime.findNthPrime()
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
class DivisibleRange:
    def __init__(self, r):
        self.r = r

    def findSmallest(self):
        import problem03
        import math
        prime = problem03.Primes()
        smallest = 1
        factors = {}
        for v in range(self.r-9, self.r+1):
            factor = prime.findLargestFactor(prime.findAllPrimeFactors(v))
            if factor != None:
                if factor[0] not in factors:
                    factors[factor[0]] = factor[1]
                elif factors[factor[0]] < factor[1]:
                    factors[factor[0]] = factor[1]
        for k in factors:
            smallest *= math.pow(k, factors[k])
        return int(smallest)

r = DivisibleRange(20)
print r.findSmallest()    
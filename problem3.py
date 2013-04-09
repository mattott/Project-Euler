""" The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?"""
class Primes:
    
    def __init__(self):
        pass
    
    def isPrime(self, value):
        if value == 2:
            return True
        import math
        square = int(math.ceil(math.sqrt(value))) + 1
        for v in range(square):
            if v > 1 and value % v == 0:
                return False
        return True
    
    def findLargestPrimeFactor(self, value):
        import math
        if self.isPrime(value):
            return value
        else:
            v = int(math.ceil(math.sqrt(value)))
            while v > 1:
                if value % v == 0 and self.isPrime(v):
                    return v
                else:
                    v -= 1
    
    def findAllPrimeFactors(self, value):
        factors = {}
        while value > 1:
            factor = self.findLargestPrimeFactor(value)
            if factor not in factors:
                factors[factor] = 1
            else:
                factors[factor] += 1
            value /= factor
        return factors
    
    def findLargestFactor(self, factors):
        import math
        largest = 0
        if factors == {}:
            return None
        for k in factors:
            temp = math.pow(k, factors[k])
            if temp > largest:
                largest = temp
                output = [k, factors[k]]      
        return output

val = Primes()
#print val.findLargestPrimeFactor(600851475143)
#print val.findAllPrimeFactors(232792560)
print val.findLargestFactor(val.findAllPrimeFactors(1))
    
                    
                    
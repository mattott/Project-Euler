"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum."""

class SumSquareDifference:
    def __init__(self, length):
        self.naturalNums = []
        for v in range(1, length+1):
            self.naturalNums.append(v)
    def getSquares(self):
        squares = []
        for v in self.naturalNums:
            squares.append(v*v)
        return squares
    def sumSquares(self):
        squares = self.getSquares()
        total = 0
        for v in squares:
            total += v
        return total
    def squareSum(self):
        total = 0
        for v in self.naturalNums:
            total += v
        return (total*total)
    def getDifference(self):
        return (self.squareSum() - self.sumSquares())

dif = SumSquareDifference(100)
print dif.getDifference()           
    
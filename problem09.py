"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

class PythagoreanTriplet:
    def __init__(self, total):
        self.total = total
        self.triplet = []
    def euclidsFormula(self, m, n):
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        self.triplet = [a,b,c]
    def sumTriplet(self):
        return self.triplet[0] + self.triplet[1] + self.triplet[2]
    def findProduct(self):
        return self.triplet[0] * self.triplet[1] * self.triplet[2]
    def findTriplet(self):
        m = 0
        while True:
            m += 1
            for n in range(1,m):
                self.euclidsFormula(m, n)
                if (self.sumTriplet() == self.total):
                    return self.findProduct()

trip = PythagoreanTriplet(1000)
print trip.findTriplet()

                    
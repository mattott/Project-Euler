class Multiples:
    
    def __init__(self):
        pass
    
    def isMultipleOf(self, v, m):
        if v % m == 0:
            return True;
        return False;

    def findAllMultiples(self, v, x, y):
        total = 0
        for n in range(v):
            if self.isMultipleOf(n, x) or self.isMultipleOf(n, y):
                total += n
        print total

matt = Multiples()

matt.findAllMultiples(1000, 3, 5)
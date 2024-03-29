"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    find the sum of the even-valued terms."""
    
class Fibonacci:
    def __init__(self):
        self.first = 1
        self.second = 2
        self.sequence = [self.first, self.second]
        self.last = 1
    
    def getNext(self):
        fibNext = self.sequence[self.last] + self.sequence[self.last-1]
        self.sequence.append(fibNext)
        self.last += 1
        return fibNext
    
    def isEven(self, n):
        if (n % 2 == 0):
            return True;
        else:
            return False;

fib = Fibonacci()
current = fib.getNext()
total = 2
while (current < 4000000):
    if fib.isEven(current):
        total += current
    current = fib.getNext()
print total

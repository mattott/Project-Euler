"""A palindromic number reads the same both ways. The largest palindrome made from the product 
    of two 2-digit numbers is 9009 = 91  99.
    Find the largest palindrome made from the product of two 3-digit numbers."""

class Palindromic():
    def __init__(self):
        pass
    def isPalindrome(self, v):
        value = str(v)
        if len(value) % 2 == 0:
            if value[:len(value)/2 - 1:-1] == value[:len(value)/2]:
                return True
            else:
                return False
        else:
            if value[:int(len(value)/2):-1] == value[:int(len(value)/2)]:
                return True
            else:
                return False
                
    #finds the largest palindrome made from the product of two x-digit numbers
    def findLargestPalindrome(self, digits):
        import math
        largest = 0
        p1 = int(math.pow(10,digits)) - 1
        p2 = int(math.pow(10,digits)) - 1
        for i in range(int(math.pow(10,digits-1)), p1):
            for j in range(int(math.pow(10,digits-1)), p2):
                if self.isPalindrome(j*i):
                    if j*i > largest:
                        largest = j*i
        return largest
            
pal = Palindromic()
print pal.isPalindrome("LAL")
print pal.findLargestPalindrome(3)
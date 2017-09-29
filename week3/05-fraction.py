
'''

A good use for OOP is to create new data types. So let's do that. We are going to create a new data type to handle fractions.

Fix the following code to be able to add and equate fractions.

'''

def gcd(m,n):
     """ Greatest Common Divisor """
     while m%n != 0:
          oldm = m
          oldn = n

          m = oldn
          n = oldm%oldn
     return n

class Fraction:
     def __init__(self):
          # top
          # bottom
          pass

     def __str__(self):
          pass

     def __add__(self,otherfraction):
          pass
          # This must return a fraction class e.g. Fraction(7,6)

     def __eq__(self, other):
          pass


    
x = Fraction(1,2)
y = Fraction(2,3)

assert x+y == Fraction(7,6)





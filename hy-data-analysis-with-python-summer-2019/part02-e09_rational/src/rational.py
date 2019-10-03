#!/usr/bin/env python3
import math

class Rational(object):
    
    def __init__(self, top, bottom):
        if bottom == 0:
            print("cannot divide by zero")
        else:
            self.numerator = top
            self.denomonator = bottom
    #maybe I don't even need to reduce? Just has to work like rational numbers!
    # If needed, could just use math.gcd instead until it's found:
    # https://docs.python.org/3/library/math.html
    
    def reduce_fraction_fast(a, b):
        """helper function, a numerator, b is denominator"""
        a = int(a)
        b = int(b) #not accepting anything other than integers so it's fine
        if a == 0 or b == 0: #b shouldn't be zero but just to be safe
            return (a, b)
        gcd = math.gcd(a, b)
        if  gcd == 1: #base case
            return(a, b) # a or b is zero or a and b are coprime
        else:
            a /= gcd
            b /= gcd #reduce
            return reduce_fraction_fast(a, b) #recurse
    
    def common_denominator(rat_1, rat_2):
        """takes two Rational objects and returns a tuple containing, in order,
        the new_rat_1.numerator, new_rat_2.numerator, common denomonator
        does not change the values of the objects
        """
        a1 = rat_1.numerator
        a2 = rat_2.numerator
        b1 = rat_1.denomonator
        b2 = rat_2.denomonator
        #get the same denominator
        a1 *= b2
        a2 *= b1
        #common denominator
        b = b1 * b2
        return (a1, a2, b)
    
    def __add__(self, rational2):    
        a1, a2, b = common_denominator(self, rational2)
        #add numerators
        a = a1+a2
        #reduce
        a,b = reduce_fraction_fast(a, b)
        return Rational(a, b)
    
    def __sub__(self, rational2):
        a1, a2, b = common_denominator(self, rational2)
        # subtract numerators
        
        a = a1 - a2
        a, b = reduce_fraction_fast(a, b)
        return Rational(a, b)
    
    def __mul__(self, rational2):
        # (almost) inverse of truediv
        a = self.numerator * rational2.numerator
        b = self.denomonator * rational2.denomonator
        a, b = reduce_fraction_fast(a, b)
        return Rational(a, b)
            
    def __truediv__(self, rational2):
        # (almost) inverse of mul, undefined where rational2.numerator is 0
        # (a/b) / (c/d) = ad/bc
        a = self.numerator * rational2.denomonator
        b = self.denomonator * rational2.numerator
        if(b == 0):
            print("can't divide by zero!")
        else:
            a, b = reduce_fraction_fast(a, b)
            return Rational(a, b)
        
    def __lt__(self, rational2):
        a, b, c = common_denominator(self, rational2)
        return a < b
    
    def __gt__(self, rational2):
        a, b, c = common_denominator(self, rational2)
        return a > b
         
    def __eq__(self, rational2):
        a, b, c = common_denominator(self, rational2)
        return a == b
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denomonator)
        
    # def reduce_fraction(top, bottom): #NOTE UNTESTED
    #     """function returns a tuple(top, bottom) in reduced form
        
    #     #recursive calls
    #     #case 1: bottom mod top == 0, e.g. 4/8 --> 8 mod 4 == 0
    #         #since 4/4 = 1 and 8/4 = 2
    #     #case 2: 
    #     #case 3: top mod bottom == 0
        
    #     #base case: a mod top == 0 and a mod bottom == 0
    #         #divide both by a and call both
        
        
    # realized I needed primes to do it efficiently
    # https://stackoverflow.com/questions/15706911/generator-in-python-generating-prime-numbers
    # going to find base case, reduce by dividing top and bottom
    # then recursing( calling the function again and the reduced top and bottom)
    # stopping when reaching max(sqrt(top), sqrt(bottom)) 
    #     """
    #     for i in range(max(top,bottom)): #going to break out of loop when small enough
    #         if i > max(math.sqrt(top), math.sqrt(bottom)): 
    #         # if n is a perfect square, sqrt(n) is the largest prime factor 
    #             # that would not have another factor found by searching
    #         # otherwise sqrt(n) is greater than any prime factor
    #         # e.g. 16. factors, 2,4,8. 2 *4 = 16, 4 * 4 = 16. You would find 2 and divide 
    #             return (top, bottom) #coprime
    #         if i % top == 0 && i % bottom == 0:
    #             top /= i
    #             bottom /= i
    #             return self(top, bottom)
                

        
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

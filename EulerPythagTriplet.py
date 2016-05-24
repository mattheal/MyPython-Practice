"""A pythagorean triplet is a set of three natural numbers, a <b <c, for which,
a^2+b^2=c^2  there exists exactly on Pythagorean triplet for which a +b +c =1000
find the product of abc"""

import math
#lets start by making some variables.

#rather than doing that lets make a series of functions that return
#the pythagorian idendities.
def pythagorianID(a,b,c):
    
def pythagorasC(a,b):
    c = math.sqrt((a**2) + (b**2))
    print c

def pythagorasB(a,c):
    b = math.sqrt((c**2) - (a**2))
    print b
    
def pythagorasA(b,c):
    a = math.sqrt((c**2) - (b**2))
    print a            

def pythagorianID(a,b,c):
    if (a**2) + (b**2) == c**2:
        return PID = True
"""#cont = 'o'
#while cont != 'no':
 #   hypot = raw_input("do you know the hypontenuse? 'y n'")
  #  Aside = raw_input("Do you know the length of side a? 'y n'")
   # Bside = raw_input("Do you know the length of side b? 'y n'")
    #if hypot.upper() == 'Y' and Aside.upper() == 'Y' and Bside.upper() == 'Y':
     #   print ('You know all the sides, there is nothing to be done')
    #elif hypot.upper() == 'N' and Aside.upper() == 'Y' and Bside.upper() == 'Y':
     #   a = float(input('How long is side a? '))
      #  b = float(input('How long is side b? '))
       # print pythagorasC(a,b)
    elif hypot.upper() == 'Y' and Aside.upper() == 'Y' and Bside.upper() == 'N':
        a = float(input('How long is side a? '))
        c = float(input('How long is side c? '))
        print pythagorasB(a,c)
    elif hypot.upper() == 'Y' and Aside.upper() == 'N' and Bside.upper() == 'Y':
        b = float(input('How long is side b? '))
        c = float(input('How long is side c? '))
        print pythagorasB(b,c)
    else:
        print('insufficient data given.... please give at least two values')

    cont = raw_input('type "no" when you are done. ').lower()"""

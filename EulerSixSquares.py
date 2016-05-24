"""The sum of the squares of the first ten natural numbers is,
1^2+2^2+.....+10^2
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2
so they want you to fine the difference in the sume of squares and the
sum of the first 100 numbers squared"""

# A simple for loop to show all squares between one and ten
for i in range(10):
    print(i, i**2)

# A more complex for loop to add these numbers together and print their sums
def sumrange(arg):
    num = 0
    for i in range(arg):
        num += i**2
        print(i, i**2)
        print("We are currently at %d " %i)
        print("The sum to this point is %d " %num)
    return num

print sumrange(10)

#Now to create a loop which will add all numbers together and then square them
def sumsqr(arg):
    num = 0
    for i in range(arg):
        num += i    
        print (num)
        print("We are currently at %d" %i)
    sqr = num ** 2
    print sqr
    return sqr
print sumsqr(10)

#The next command will find the difference between the results of both functions

print (sumsqr(101) - sumrange(101)) 

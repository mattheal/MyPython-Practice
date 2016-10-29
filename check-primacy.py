#!/user/bin/python
#checking if a number is prime.... I'm starting to feel like this class
#Is a demonstration of the Euler challenges...
#I'm going to modify for user input again


def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print (("{} equals {} x {} ".format(n, x, n // x)))
            return False
    else:
        print(n, "is a prime number")
        return True


def userput():
    lastval = input("What is the highest prime you want to check?  ")
    int(lastval)
    return lastval


def main():
    usemax = userput()
    for n in range(1, usemax):
        isprime(n)

main()
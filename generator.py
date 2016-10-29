#!/user/bin/python
#Lynda generator function for class


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1


for n in primes():
    if n > 100: break
    print(n)

'''
def userput():
    lastval = input("What is the highest prime you want to check?  ")
    int(lastval)
    return lastval


def main():
    usemax = userput()
    for n in range(1, usemax):
        isprime(n)

main()
'''
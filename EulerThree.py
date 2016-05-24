"""This function will find the prime numbers """
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def isprime(n):
    p = True
    if n ==2 or n == 3: return True
    if n < 2 or n %2 == 0 : p = False
    if n < 9 : p = True
    if n % 3 == 0 : p = False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print '\t',f
        if n % f ==0: print n
        if n%(f+2)==0:print (n, f)
        f += 6
        return True

print isprime(5005)
        
    

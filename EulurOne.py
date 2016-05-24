#Find all multiples of 3 or five below 1000
summA = 0
summB = 0
for num in range(1000):
    if num % 3 == 0:
        summA += num
        print (num, num / 3)    
    elif num % 5 == 0:
        summB += num
        print (num, num / 5)   

print ("The sum of all multiples of 3 is %d " %summA)
print ("The sum of all multiples of 5 is %d " %summB)
sumtot = summA + summB
print ("The sum of all listed multiples is %d " %sumtot)

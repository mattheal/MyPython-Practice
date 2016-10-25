#!/usr/bin/python
#If the numbers 1 to 5 are written out in words: one, two, three, etc then 
#there are 3+3+5=14 letters in total if all the numbers from 1 to 1000 were writ#written out in words, how many letters would be used?

#first create an index that links various numbers to the number of letters
#to spell the associated number first 1 - 19 then by tens 20 - 100
#then by hundreds 100 - 1000 all numbers between whill be combinations of these
#associated numbers

num2letter = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8, 0: 4 }

#next create a function that will link the numbers to their number of letters
def numbercount():
	total20 = 0
	total100 = 0
	total1000 = 0
	for num in range(1000):
		if num <= 20:
		#now I just need to remember how to pull values from an index
			value_at_index = num2letter.values()[num]
			total20 += value_at_index
			print total20
		elif num >= 100:
			value_at_index = num2letter.values()[num]
			if not num:
				value_at_index =
		

numbercount()	

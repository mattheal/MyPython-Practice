#!/usr/bin/env python
#This is a python script that will assign each student a job based on a random number

import random

#This is the primary engine of the program
def my_number():
	number = random.randint(1, 10)
	return number
'''	if dice_roll == 6:
		print "Congradulations a perfect roll"
	elif dice_roll >= 4:
		print "Not too shaby"
	else:
		print "Report to the department of sociatal clensing" '''

#This definition allows the user to determine the number of iterations of the engine function
'''def personal():
	players = input("How many people will be playing today? ")
	return players'''

#This calls the program engine $studnets number of times
def main():

	gameover = False
	comp_num = my_number()

	while gameover == False:
		###players = personal()

		user_choice = input("Choose a number between one and ten? ")
		int(user_choice)

		if user_choice <= 0:
			print ("No it has to be between one and ten")
		elif user_choice >= 11:
			print ("Seriously, no dude, between one and ten!")
		elif user_choice > comp_num:
			print ("You're too high")
		elif user_choice < comp_num:
			print ("You're too low")
		else:
			print ("Congradulations you are the winner")
			gameover = True
		
			
main()

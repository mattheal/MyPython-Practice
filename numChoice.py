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

		user1_choice = input("Choose a number between one and ten player 1? ")
		int(user1_choice)
		user2_choice = input("Choose a number between one and ten, player2? ")
		int(user2_choice)
		user1dist = abs(comp_num - user1_choice)
		user2dist = abs(comp_num - user2_choice)

		
		if user1dist < user2dist:
			print ("Player1 chose %s player2 chose %s the actual number is %s player1's choice was %s from the correct number, player one is the winner" % (user1_choice, user2_choice, comp_num, user1dist))
			gameover = True
		elif user2dist < user1dist:
			print ("Player1 chose %s player2 chose %s the actual number is %s player2's choice was %s from the correct number, player TWO is the winner" % (user1_choice, user2_choice, comp_num, user2dist))
			gameover = True
		elif user2dist == user1dist:
			print ("Player1 an player2 both chose numbers %s away from the correct answer %s it's a tie! try again " % (user2dist, comp_num))
		else:
			print ("It's not going to work if you guys choose the same numbers! %s %s" (user1_choice, user2_choice)) 
		
			
main()

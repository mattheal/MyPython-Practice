#!/usr/bin/env python
#This is a python script that will assign each student a job based on a random number

import random

#This is the primary engine of the program
def roll_em():
	dice_roll = random.randint(1, 6)
	return dice_roll
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
	players_array = []
	tie = True

	while tie == True:
		###players = personal()
		for i in range(2):
			player_roll = roll_em()
			players_array.append(player_roll)
			print "palyer %s has rolled a %s " % (i+1, player_roll)
		
		if players_array[0] > players_array[1]:
			print "Player 1 is the winner"
			tie = False
			return tie
		elif players_array[1] > players_array[0]:
			print "Player 2 is the winner"
			tie = False
			return tie
		else:
			print "It's a tie"
			del players_array[:]

#This calls the actual function
main()

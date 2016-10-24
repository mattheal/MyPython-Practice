#!/usr/bin/env python
#This is a python script that will assign each student a job based on a random number

import random

#This is the primary engine of the program
def position_assigner():
	assigned_position = random.randint(0, 10000)
	if assigned_position == 10000:
		print "Congradulations you are the president"
	elif assigned_position >= 9990:
		print "You have been selected to serve in the senate"
	elif assigned_position >= 9900:
		print "You have been assigned to serve as a judge"
	elif assigned_position >= 9500:
		print "You are an attorney"
	elif assigned_position >= 8900:
		print "You are a police officer"
	elif assigned_position >= 8000:
		print "You are a government beaurocrat"
	elif assigned_position >= 7500:
		print "You are a military officer"
	elif assigned_position >= 6800:
		print "You are a professional worker"
	elif assigned_position >= 3300:
		print "You are a you are a lower enlisted draftee"
	elif assigned_position >= 1500:
		print "You are a common laborer, due to the American Patriot Workers Act"
		print "You are required to work no less than 65 hours a week"
		print "The tax rate is set at 65%"
	else:
		print "Report to the department of sociatal clensing"

#This definition allows the user to determine the number of iterations of the engine function
def personal():
	students = input("How many students are we placing today? ")
	return students

#This calls the program engine $studnets number of times
def main():
	students = personal()
	for i in range(students):
		position_assigner()

#This calls the actual function
main()

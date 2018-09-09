#!/usr/bin/env python3
import math

class Line:

	def __init__(self, coorda, coordb):
	#	coorda = tuple(float(x.strip()) for x in raw_input().split(','))
	#	coordb = tuple(float(x.strip()) for x in raw_input().split(','))
		self.coorda = coorda
		self.coordb = coordb

	def distance(self):
		a = abs(self.coorda[0] - self.coordb[0])
		b = abs(self.coorda[1] - self.coordb[1])
		c = math.sqrt(a**2 + b**2) 
		return c

	def slope(self):
		run = abs(self.coorda[0] - self.coordb[0])
		rise = abs(self.coorda[1] - self.coordb[1])
		m = rise/run
		return m

my_line = Line((0,0),(2,2))

print(my_line.distance())
print(my_line.slope())

def gameon():
	end = False

	while not end:
		print("Enter the first coordinate ")
		coor1 = tuple(float(x.strip()) for x in input().split(','))
		print("Enter the second coordinate ")
		coor2 = tuple(float(x.strip()) for x in input().split(','))
		test_line = Line(coor1,coor2)
		print("The distance between ",coor1," and ",coor2," is: ",test_line.distance())
		print("The slope between ",coor1," and ",coor2," is: ",test_line.slope())
		option = input("Would you like to play again? ")
		if option[0].lower() == 'y':
			continue
		else:
			end = True

gameon()
	

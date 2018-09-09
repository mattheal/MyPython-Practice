#!/usr/bin/env python3
import math

class Cylinder:
	
	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		vol = math.pi*(self.radius**2)*self.height
		return vol

	def surface_area(self):
		area = self.height*(2*math.pi*self.radius)
		return area
test_cylinder = Cylinder(2,2)

print(test_cylinder.volume())
print(test_cylinder.surface_area())

def gameon():
	end = False
	while not end:	
		radius = int(input("What is the radius of your cylinder? "))
		height = int(input("What is the height of your cylinder? "))
		my_cyln = Cylinder(height,radius)
		print(my_cyln.volume())
		print(my_cyln.surface_area())
		choice = input("Would you like to keep playing: ")
		if choice[0] == 'y':
			continue
		else:
			end = True


gameon()

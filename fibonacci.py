#!/usr/bin/python

#fibonacci series as descibed in lynde.com python trahing course

#I'm going to take it a step further and add some user input

#Now that that is working I'm going to practice functions by separating
#each part of the code into a differnt function


def main():
    print ("Welcome to my simple fibonacci sequencer :) ")
    theloop()


def userput():
    ending = input("At what number do you want the sequence to end? ")
    return ending


def theloop():
    a, b = 0, 1
    ending = userput()
    while b < ending:
        print(b)
        a, b = b, a + b
    print (("These are all the numbers in the sequence up to %s " % (ending)))

main()
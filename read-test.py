#!/usr/bin/python

#read the lines from a document, useful program from a lynda class
#modified to add user input, untested

text = input('what file would you like to open? Include the path')

fh = open(text)
for line in fh.readlines():
    print(line, end=' ')
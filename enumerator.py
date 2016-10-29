#!/usr/bin/python
#enumerting iterators

'''
def main():
    s = 'this is a string.'
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))


main()
'''
def main():
    s = strings()
    for index, line in enumerate(s):
        print(index, line)
        if line == 's':
            print('index {} is an s'.format(index))


def strings():
    s = input("Enter a string to iterate: ")
    str(s) #it keeps telling me their is an error around selectable
    #user input I will have to sit on this and get back to it later
    #the simplified function works just fine
    return s


main()

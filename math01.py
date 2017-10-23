# my first script I wrote which works. It's just mod 25 math

import sys # imports stuff. Not sure if this is actually necessary.

while 1==1: # prepares a loop  
    a = int(input("What is A? Must be 25 of under: "))
    # lets you input numerical value of variable A
    b = int(input("What is B? Must be 25 of under: "))
    # lets you input numerical value of variable B

    if a + b > 25: # conditional statement which introduces mod 25
        mod = (a + b) - 25 # intitiates mod 25 if A+B is over 25
        print(mod)# tells program to print 'mod' after mod 25
    # I made 'mod' a variable with the attribute of an equation
    else:
        print(a + b) # if A+B is under 25 it prints the answer

    input("Press any key to start again. ")
    # initiates the loop so game starts over



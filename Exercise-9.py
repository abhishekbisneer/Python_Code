#Guessing Game One   
#Exercise 9 (and Solution)
'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random as rd
import sys

userinput=0
rand=rd.randint(1,9)    
print(rand)
attempt=0

while (userinput!=rand) or userinput=='exit':    
    userinput=input("Enter a number: \n>>>")
    attempt=attempt+1        
    if userinput=='exit':
        print("Sorry. User chose to exit.")
        break    
    if rand>int(userinput):
        userinput=input("Guess high:\n >>>")
    if rand<int(userinput):
        userinput=input("Guess low:\n >>>")
    if rand==int(userinput):
        print("\n Congrats!! Right Guess")
    
    
print("\n Number of attempts: {0}".format(attempt))

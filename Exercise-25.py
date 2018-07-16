#Exercise 25
'''
In a previous exercise, we've written a program tsat "knows" a number and asks a user to guess it.
This time, we're going to do esactly the opposite. You, the user, will have in your head a number between 0 and 100. 
The [rogram will guess a number.
At the end of hthis exchange, your program should print out hown many guessess it took to get your number.
As the writer of this program, you will have to choose how your program will stratigically guess. 
A naive strategy can be to simply sraart the guessing at 1, and keep going (2,3,4 ..etc.) until
you hit the number. But that's not an otimal guessingstrategy. An alternated straregy might be to 
guess 50 (right in the middle of the range), and then increase/decrease by 1 as needed. 
After you've written the program, try to find the optimal strategy!
(we will talk what is the optimal one next week with the solution)
'''
import random

#random.randint()
user_num=80
attempts=0
min_num=1
max_num=100
sys_num=random.randrange(min_num,max_num,1)
while user_num!=sys_num:
    attempts=attempts+1
    if sys_num==user_num:
        break
    elif sys_num>user_num:
        max_num=sys_num
    elif sys_num<user_num:
        min_num=sys_num
        
    print("\nAttempts = {}".format(attempts))
    print("Sys Guess = {}".format(sys_num))        
    sys_num=random.randrange(min_num,max_num,1)
    
    
print("\nThe system guess is {}".format(sys_num))
print("Attempts = {}".format(attempts))
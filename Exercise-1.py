# Exercise 1
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
import time

class cal:    
    def abc(age):
        #self.age=age
        t=time.localtime()
        HundredthYear=t[0]+(100 - age)
        return HundredthYear
    
    def numoftimestobeprinted():        
        num=int(input("please enter the num of time the statement to be printed: \n>>>"))
        return(num)
        
    username=input("Please eneter your Name :\n>>>")
    age=int(input("Please eneter your Age :\n>>>"))
    k=abc(age)
    print("\nHi {0}, You will turn 100 years in {1}\n".format(username,k))
    
    for i in range(0,numoftimestobeprinted()):
        print("\n{0}. Hi {1}, You will turn 100 years in {2}".format(i,username,k))



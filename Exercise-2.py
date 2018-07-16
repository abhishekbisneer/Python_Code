#Exercise 2 (and Solution)
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message
'''

def checkint(userinput):
    try:
        int(userinput)
        return int(userinput)
    except:
        return 0

userinput=input("\nPlease provide a number:\n>>>>")

k=checkint(userinput)

if k != 0:
    if k%2==0:
        print("Provided number is EVEN\n") 
    else:
        print("Provided number is ODD\n")
        
    if k%4==0:
        print("Divsible by 4\n")
    else:    
        print("NOT Divsible by 4\n")              

    print("Please provide 2 number:")
    num=int(input("Number 1:"))
    check=int(input("Number 2:"))
    
    if num%check==0:
        print("The proided numbers {0} and {1} are divisabel".format(num,check))
    else:
        print("The proided numbers {0} and {1} are NOT divisabel".format(num,check))

else:
    print("\nProvided number\n")



'''
       
        if k%4==0:
            print("\nNumber is divisabe by 4")
        else:
            print("\nNumber is NOT divisabe by 4")
            '''
#Check Primality Functions   
#Exercise 11 (and Solution)
'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
'''
def userinput():
    return(int(input("Please provide a num: ")))

def checkprime(num):
    divrange=num/2
    if divrange<=1:
        return("Please chose a num greater than 2")
    else:
        z=[]
        divrange=int(num/2)
        
        if divrange==1:
            divrange==2
            
        for i in range(2,divrange+1):
            if num%i==0:
                z.append(i)
        
        if len(z)==0:
            return("The number is a prime number")
        else:
            return("The number is diviabel by: {0}".format(z))
            

num=userinput()
print(num)

result=checkprime(num)
print(result)

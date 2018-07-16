# Fibonacci  
# Exercise 13 (and Solution)
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then 
generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence 
is the sum of the previous two numbers in the sequence. The sequence looks like this: 
    1, 1, 2, 3, 5, 8, 13, …)
'''


fib=[]

Total=int(input("Please provide the number of fibonacci numbers required: "))
i=0
j=0
while i!=Total-1:
    i=len(fib)
    if len(fib)<2:
        j=j+1
        fib.append(j)
    else:
        a=fib[len(fib)-2]
        b=fib[len(fib)-1]
        c=a+b
        fib.append(c)
                
print(fib)

print("---------------------------------------")

def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
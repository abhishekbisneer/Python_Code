#Exercise 3 (and Solution)

'''
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
write a program that prints out all the elements of the list that are less than 5.

Extras:
Instead of printing the elements one by one, make a new list that has all the elements less than 5 and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the 
original list 'a' that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i < 5:
        b.append(i)        
print("The values of list 'a' which are less than 5- {0}".format(b))

userinput=int(input("Please provide a number: \n>>>>"))
c=[]
for i in a:
    if i < userinput:
        c.append(i)
print("The values of list 'a' which are less than user input {0} - {1}".format(userinput,c))        
        
        

        


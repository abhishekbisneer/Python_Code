#List Remove Duplicates  
#Exercise 14 (and Solution)
'''
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, 
and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
x=[2,1,2,1,4,5,6,7]
z=[]
for i in range(0,len(x)):
    if x[i] not in z:
        z.append(x[i])        
print(z)        

print("----------------------------------------------------")

# there is some error 
# Application throws error "list object cannot be called"
#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print (a)
print (dedupe_v2(a))
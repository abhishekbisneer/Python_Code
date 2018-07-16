# List Ends 
# Exercise 12 (and Solution)
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
'''

a = [5, 10, 15, 20, 25]
b=[]
print(a[0])

b.append(a[0])
b.append(a[len(a)-1])
print(b)


print("----------------------------------")

def extractlast(a):
    return [a[0],a[len(a)-1]]

a = [5, 10, 15, 20, 25]
print(extractlast(a))

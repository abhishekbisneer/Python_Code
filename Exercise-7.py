#List Comprehensions  
#Exercise 7 (and Solution)
'''
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list 'a' and makes a new list 
that has only the even elements of this list in it.
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]

for i in range(len(a)):
    print(a[i])
    if a[i]%2 == 0:
        b.append(a[i])
print(b)

print("-------------------------------------------------")

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]

print(b)
        
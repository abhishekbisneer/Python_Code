#List Overlap  
#Exercise 5 (and Solution)
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program works on 
two lists of different sizes.

Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point 
- we’ll get to it soon)
'''
import random
print("---------------------------------------------------------")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a) & set(b)))

print("---------------------------------------------------------")

a = random.sample(range (10),5)
b = random.sample(range (20),15)
e=[]
for i in a:
    for j in b:
        if i == j:
            e.append(i)
            
f=list(set(e))
print(f)            

print("---------------------------------------------------------")


import random
x = random.sample(range (10),5)
y = random.sample(range (20),15)
print(x)
print(y)
a= []
for num in x:
    if num in y:
        a.append(num)

print(a)

print("---------------------------------------------------------")

a = random.sample(range (10),5)
b = random.sample(range (20),15)
print(a)
print(b)
e=[]
for i in a:
    if i in b:
        e.append(i)

print(e)            
print(list(set(e)))
 
print("---------------------------------------------------------")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num=[]
for i in a:
    if (i in b) and (i not in num):
        num.append(i)
print(num)


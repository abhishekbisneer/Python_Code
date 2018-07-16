#Reverse Word Order   
#strings
#Exercise 15 (and Solution)
'''
Write a program (using functions!) that asks the user for a long string containing multiple 
words. Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:

My name is Michele
Then I would see the string:

Michele is name My
'''  

print("-------------------------------------------")   

str="My name is Michele"
k=str.split()
result=" ".join(k[::-1])
print(result)

print("-------------------------------------------")

str="My name is Michele"
rev=""
for i in reversed(str):
    rev=rev+i
    
print(rev) 

print("-------------------------------------------")   

str="My name is Michele"
print(str[::-1])

print("-------------------------------------------")   

k="My name is Michele"
x=k.split(" ")
print(x)
x=x[::-1]
j=""
for i in range(0,len(x)):
    j=j+" " + x[i]
print(j)

# Exercise 23 (and Solution)
'''
Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number. 
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
The explanation is easier with an example, which I will describe below.)

Discussion
You’ll need to stitch together a few ideas of things I’ve previously talked about on this blog, so if you need a refresher in any of these topics, now is your chance! Of course, there are any number of ways to do this exercise, so these are only suggestions.

Topics:
Reading a file, in Exercise 21
Number types and converting to integers from strings, in Exercise 1
Lists, in Exercise 3 and Exercise 5
'''
# Text files used and are saved at the locaiton "E:\Python\Practice"
#Prime Numbers.txt
#Happy Numbers.txt
L1=[]
L2=[]

with open("Prime Numbers.txt","r") as f1:
    line=f1.readline()
    while line:
        L1.append(line.strip())
        line=f1.readline()
        
with open("Happy Numbers.txt","r") as f2:
    line=f2.readline()
    while line:
        L2.append(line.strip())
        line=f2.readline()
    
print(L1)
print(L2)

result=[a for a in L1 if a in L2]
print(result)
print("------------------------------------------------------------")
result2=[a for a in result if result.count(a)==1]
print(result2)

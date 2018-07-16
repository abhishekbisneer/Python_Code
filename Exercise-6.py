#String Lists  
#strings lists index
#Exercise 6 (and Solution)
'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

print("-------------------------------------------------")

str="abcd"
str="civic"
str="repaper'"
palcheck=""
for i in range(0,len(str)):
    print("'{0}' -- '{1}'".format(str[i],str[len(str)-(i+1)]))
    if str[i]!=str[len(str)-(i+1)]:
        palcheck="no"
if palcheck=="no":
    print("Not a palindrome")            
else:
    print("Palindrome")
    
    
print("-------------------------------------------------")

str="abcd"
rev=str[::-1]
print(rev)
if str==rev:
    print("Palindrome")
else:
    print("Not a palindrome")    
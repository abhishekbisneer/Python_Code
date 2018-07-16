#Birthday Dictionaries 
#Exercise 33 (and Solution)
'''
This exercise is Part 1 of 4 of the birthday data exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.
For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
'''

bday={'Arjun':'26-Oct-1986','Abhishek':'14-Jan-1986'}
def userinput(bday):
    #k=list(bday.keys())
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in bday:
        print(i)
    user_in=input("Who's birthday do you want to look up?\n>>>")
    if user_in in bday:
        print("{} Birthday is on {}".format(user_in,bday[user_in]))
    else:
        print("\n {}'s Birthday is not available".format(user_in))

if __name__=="__main__":
    userinput(bday)
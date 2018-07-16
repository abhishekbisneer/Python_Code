#Birthday Json  
#Exercise 34 (and Solution)
'''
This exercise is Part 2 of 4 of the birthday data exercise series. 
The other exercises are: Part 1, Part 3, and Part 4.
In the previous exercise we created a dictionary of famous scientists’ birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary 
from a JSON file on disk, rather than having the dictionary defined in the program.
Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientist’s name. 
If you run the program multiple times and keep adding new names, 
your JSON file should keep getting bigger and bigger.
'''
import json

def user_cont():
    print("Weleome!! we have the birtdays of")
    with open("Bday.json","r") as f:
        info=json.load(f)
        for i in info:
            print(i)        
    user_in=input("Who's birthday do you want to look up?\n>>>")
    if user_in in info:
        print("\n{}'s birthday is on {}".format(user_in,info[user_in]))
    else:
        write_content(user_in,info)
        
def write_content(user_in,info):
    user_in2=input("Hi user, as we donot have teh B'day of {}, could you please provide the info, \n we could build our Data Base\n>>>".format(user_in))
    dict_2={user_in:user_in2}
    info.update(dict_2)
    print(info)

    with open("Bday.json","a+") as f:
        json.dump(info,f)

    with open("Bday.json","r") as f:
        k=json.load(f)
        for i in k:
            print(i)  
            
if __name__=="__main__":
    bday={"Vikram":"14-Nov-2018","Arjun":"26-Oct-1986","Ad":"01-Jun-1984"}
    with open("Bday.json","w") as f:
        json.dump(bday,f)
    user_cont()
    
    
    
    
    

#Read From File 
#Exercise 22 (and Solution)
'''
Given a .txt file that has a list of a bunch of names, 
count how many of each name there are in the file, 
and print out the results to the screen. 
I have a .txt file for you, if you want to use it!

Extra:
Instead of using the .txt file from above (or instead of, if you want the challenge), 
take this .txt file, and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene 
recognition database, and lists the file directory hierarchy for the images. 
Once you take a look at the first line or two of the file, it will be clear 
which part represents the scene category. To do this, you’re going to have to remember 
a bit about string parsing in Python 3. I talked a little bit about it in this post.
'''
'''
unique_names=[]
names=[]
with open("Test.txt","r") as f:
    for i in f.readlines():
        names.append(i.replace("\n","").strip())
        if unique_names.__contains__(i.replace("\n","").strip()):
            pass
        else:
            unique_names.append(i.replace("\n","").strip())
            
print(names)
print(unique_names)            

for i in range(0,len(unique_names)):
    k=names.count(unique_names[i])
    print("{0} - Count = {1}".format(unique_names[i],k))
'''

counter_dict = {}
with open('Test.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

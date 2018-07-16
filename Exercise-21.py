#Write To A File 
#Exercise 21 (and Solution)
'''
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, 
use the code from the solution), and instead of printing the results to a screen, 
write the results to a txt file. In your code, 
just make up a name for the file you are saving to.

Extras:
Ask the user to specify the name of the output file that will be saved.
'''

from bs4 import BeautifulSoup as bs
import requests

base_url = 'http://www.nytimes.com'
data=requests.get(base_url)
soup=bs(data.text)#,"html.parser")
with open("Test.txt","w") as f:
    for paragraph in soup.find_all(Class_="story-heading"):
        if paragraph.a:
            f.write(paragraph.a.text.replace("\n"," ").strip())
        else:
            f.write(paragraph.content[0].strip())
    
'''
if __name__=="__main__":    
    base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"        
    data=urllib.request.urlopen(base_url).read()
    data1=data.decode("utf-8")
    with open("Test.txt","w") as openfile:
        #for paragraph in data1.find("title"):
        openfile.write(data1)
'''
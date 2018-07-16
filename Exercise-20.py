#Element Search 
#Exercise 20 (and Solution)
'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.

Extras:
Use binary search.
'''
'''
def find_num(num,l1):
    numexists=""
    for i in range(0,len(l1)-1):
        if l1[i]==num:
            numexists="yes"
            break      
        
    if numexists=="":
        return("Number does not exist")
    else:
        return("Number exist")

if __name__=="__main__":
    l1=[1,2,3,4,5,6,7,8,9]
    num=input("please provide a number: ")
    print(find_num(num,l1))
'''
'''
l1=[1,2,3,4,5,6,7,8,9]
num=int(input("please provide a number: "))
start=0
end=len(l1)
count=0
result="Number does not exist"
while count!=2:
    mid=int(((end-start)/2)+start)
    if num>l1[mid]:
        start=mid
        end=end
        count=end-start
    elif num<l1[mid]:
        start=end
        end=mid
        count=end-start
    else:
        result="Number exists"
        break


print(result)

'''
def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index
  
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True
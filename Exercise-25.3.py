import random

#random.randint()
def guess_num(min_num,max_num):
    attempts=0
    sys_num=random.randrange(min_num,max_num,1)

    while user_num!=sys_num:
        attempts=attempts+1
        sys_num=random.randrange(min_num,max_num,1)            
        print("\nAttempts = {}".format(attempts))
        print("Sys Guess = {}".format(sys_num))        
        if sys_num==user_num:
            break
        elif sys_num>user_num:
            max_num=sys_num
        elif sys_num<user_num:
            min_num=sys_num


if __name__=="__main__":
    min_num=1
    max_num=100
    user_num=80
    if user_num>50:
        min_num=50
        guess_num(min_num,max_num)
    elif user_num<=50:
        max_num=50
        guess_num(min_num,50)

sys_num=random.randrange(min_num,max_num,1)
while user_num!=sys_num:
    attempts=attempts+1
    print("\nAttempts = {}".format(attempts))
    print("Sys Guess = {}".format(sys_num))        
    sys_num=random.randrange(min_num,max_num,1)
    
    
print("\nThe system guess is {}".format(sys_num))
print("Attempts = {}".format(attempts))
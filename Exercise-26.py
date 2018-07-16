#Check Tic Tac Toe Solutions  
#Exercise 26
'''
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 1, Part 3, and Part 4.
As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, 
not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
and a 2 means that player 2 put their token in that space.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
Don’t worry about the case where TWO people have won - 
assume that in every board there will only be one winner.

Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
'''


def row_check(l):
    for r in range(0,2):
        if 0 not in l[r]:
            if l[r][0]==l[r][1] and l[r][1]==l[r][2]:
                return "row wins"
    return "row fails"         

def col_check(l):
    for c in range(0,2):
        if (l[0][c]!=0) and (l[1][c]!=0) and (l[2][c]!=0):
            if l[0][c]==l[1][c] and l[1][c]==l[2][c]:
                return "Col wins"
    return "Col fails"         

def diagnol_check(l):
    if (l[0][0]!=0) and (l[1][1]!=0) and (l[2][2]!=0):
            if l[0][0]==l[1][1] and l[1][1]==l[2][2]:
                return "Diagnol wins"
    return "Diagnol fails"         


#winner_is_2 
L1= [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

#winner_is_1 
L2= [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

#winner_is_also_1 
L3= [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

#no_winner 
L4= [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

#also_no_winner 
L5= [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]        

def consol(*lists):    
    biglist=[]
    for items in lists:
        biglist.append(lists)
    return biglist
        
if __name__=="__main__":
    biglist=[]
    biglist.append(consol(L1,L2,L3,L4,L5))    
    #consol(L1,L2,L3,L4,L5)
    print(len(biglist))
    print(biglist)
    for i in range(0,len(biglist)):
        l=[]
        l=biglist[i]
        print("--------------------------------------")
        print("LIST {}".format(i+1))
        print(row_check(l))
        print(col_check(l))
        print(diagnol_check(l))

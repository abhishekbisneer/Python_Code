'''
L1= [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

#winner_is_1 
L2= [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
'''
L1=[[1,2,3],[4,5,6]]
L2=[[7,8,9],[10]]

def consol(*lists):    
    lists=list(lists)
    biglist=[]
    print(len(lists))
    biglist.append(lists)
    #for i in range(0,len(lists)):
    #    biglist.append(lists)
    return biglist
        
if __name__=="__main__":
    biglist=[]
    #biglist.append(consol(L1,L2,L3,L4,L5))
    biglist=consol(L1,L2)
    print(biglist)

[([[2, 2, 0], [2, 1, 0], [2, 1, 1]], [[1, 2, 0], [2, 1, 0], [2, 1, 1]]), 
 ([[2, 2, 0], [2, 1, 0], [2, 1, 1]], [[1, 2, 0], [2, 1, 0], [2, 1, 1]])]
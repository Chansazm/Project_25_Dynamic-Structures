class Solution:    
    def fib(self,n:int)->int:
        Table = [None] * (n+1)
        Table[1] = 1
        
        for i in range(3,n+1):
            Table[i] = Table[i-1] + Table[i-2]
        return Table[n]

    print(fib(6)) #

def cansum(target,nums):
    Table = [False] * (target + 1)
    Table[0] = True
    print(Table)
    
#print(cansum(7,[5,3,4,6]))
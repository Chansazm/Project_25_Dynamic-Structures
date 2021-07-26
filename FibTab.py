def fib(n):
    Table = [None] * (n+1)
    Table[1] = 1
        
    for i in range(3,n+1):
        Table[i] = Table[i-1] + Table[i-2]
    return Table[n]

print(fib(6)) #


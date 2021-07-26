def cansum(targetsum,numbers):
    Table = [False] * (targetsum+1)
    Table[0] = True
    
    for i in range(targetsum):
        if Table[i] == True:
            for num in numbers:
                Table[i+num] = True
    print(Table)
    return Table[targetsum]
                
#Driver function
print(cansum(7,[5,4,3,7])) #->True
 
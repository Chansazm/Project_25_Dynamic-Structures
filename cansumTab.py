def cansum(targetsum,numbers):
    Table = [False] * (targetsum+1)
    Table[0] = True
    
    for i in range(len(numbers)-1):
        if numbers[i] == True:
            for num in numbers:
                numbers[i+num] = True
    return Table[targetsum]
                






#Driver function
print(cansum(7,[5,4,3,7])) #->True
 
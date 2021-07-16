def cansum(target,numbers,memo = {}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False
    
    for each_value in numbers:
        remainder = target - each_value
        if cansum(remainder,numbers,memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False


#Driver function
print(cansum(7,[5,3,4,7]))
print(cansum(700,[5,3,4,7]))
        
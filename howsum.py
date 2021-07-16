def howsum(target,nums,memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for values in nums:
        remainder = target - values
        remainder_result = howsum(remainder,nums,memo)
        if remainder_result != None:
            memo[target] = [*remainder_result,values]
            return memo[target]
    memo[target] = None
    return memo[target]

#Driver function
print(howsum(7,[5,3,4,7]))
print(howsum(7,[5,3,4,7]))
#print(howsum(7,[2,4]))
        
def twosum(nums,target):
    values_map = {}
    for key,value in enumerate(nums):
        values_map[value] = key
        diff = target - value
        if diff in values_map:
            return [key, values_map[diff]]

#Driver function
nums = [2,5,7,4]
target = 9
print(twosum(nums,target))
        
        
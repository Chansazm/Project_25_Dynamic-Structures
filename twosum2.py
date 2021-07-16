def twosum2(nums,target):
    dict = {}
    for key,value in enumerate(nums):
        difference = target - value
        if difference in dict:
            return [key,dict[difference]]
        dict[value] = key
    return []

#driver function
nums = [3,2,4]
target = 6
print(twosum2(nums,target))
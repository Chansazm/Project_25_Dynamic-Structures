import math

def bestsum(target, nums,memo={}):
    if target in memo: return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = math.inf
    for values in nums:
        remainder = target - values
        remainder_result = bestsum(remainder, nums,memo)
        if remainder_result != None:
            combination = [*remainder_result, values]
            if shortest_combination == math.inf or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[target] = shortest_combination
    return shortest_combination


print(bestsum(10,[1,3, 4]))  # [3,3,4]


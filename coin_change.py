def coin_change(target,coins,memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    best_change = None
    for change in coins:
        remainder = target - change
        combination = coin_change(remainder,coins,memo)
        if combination != None:
            result = [*combination, change]
            if best_change == None or len(result)< len(best_change):
                best_change = result
    memo[target] = best_change
    return best_change

print(coin_change(6,[1,3, 4]))  # [3,3]
print(coin_change(100,[1,3, 4]))

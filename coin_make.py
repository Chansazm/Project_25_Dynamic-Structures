import sys

def coin_change(coins, remainder, cache):
    if remainder < 0:
        return -1

    if remainder == 0:
        return 0

    if cache[remainder] != 0:
        return cache[remainder]

    system_max = sys.minsize
    minimum = system_max
    for coin in coins:
        change_result = coin_change(coins, remainder - coin, cache)

        if (change_result >= 0 and change_result < minimum):
            minimum = 1 + change_result

    cache[remainder] = -1 if (minimum == system_max) else minimum

    return cache[remainder]
print(coin_change(6,[1,3, 4],0))  # [3,3]
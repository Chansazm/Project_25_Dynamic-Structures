def solve(a):
    max = 0
    for x in range(len(a)):
        if a[x] > max:
            max = a[x]
    return max


print(solve([3,8,2,9,-45,88,9]))
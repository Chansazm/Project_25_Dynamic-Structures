def Knapsackproblem(items,capacity):
    Knapsack = [[0 for x in range(0,capacity+1)]for y in range(0,len(items)+1)]
    print(Knapsack)

print(Knapsackproblem([[]],10))
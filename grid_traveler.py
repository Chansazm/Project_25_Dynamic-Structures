def grid_traveler(m,n):
    if m and n == 1: return 1
    if m or n == 0: return 0
    return grid_traveler(m-1,n) + grid_traveler(m,n-1)
       
print(grid_traveler(2,3)) 
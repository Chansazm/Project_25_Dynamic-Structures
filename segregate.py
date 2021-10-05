def segregate(arr,n):
    count = 0
    #count number of zeros
    for i in range(0,n):
        if arr[i] == 0:
            count += 1
    #fill array with zeros first
    for i in range(0,count):
        arr[i] = 0
    
    #fill remaining space with ones   
    for j in range(count,n):
        arr[j] = 1
    return arr


#Driver function
array = [0,1,1,0]
n = len(array)
print(segregate(array,n)) #count = 4
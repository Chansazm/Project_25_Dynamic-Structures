def divisor(A,B):
    if A>B:
        A,B = B,A
        if B>=A and  B%A == 0:
            print("A is {} and B is {}".format(A,B),"Result is {}".format(B//A))
      
            
#Driver function
print(divisor(8,4)) #

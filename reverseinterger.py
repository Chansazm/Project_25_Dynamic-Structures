def reverse(n):
    x = 0
    while n:
        x = modulus(n)
        y = division(x)

def modulus(num):
    if num < 0:
        return num % -10
    else:
        return num % 10

def division(num):
    return num//10
    


print(modulus(-123))
print(division(12)) #1

"""Requirements
input: 123 or -123 -> 321 or -321
123%10 ->3
result
3

1. calculate modulus
2. Calculate division
3. add to result


"""
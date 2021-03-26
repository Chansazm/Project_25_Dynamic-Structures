def parentheses(s):
    counter = 0
    for char in s:
        if char == '(':
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1  
    return counter == 0

#Driver function
print(parentheses('(())')) #True
print(parentheses('(()')) #False
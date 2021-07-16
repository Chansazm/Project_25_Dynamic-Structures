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

def parentheses2(s):
    stack = []
    lookup = {'(': ')', '{': '}', '[' : ']'}
    for p in s:
        if p in lookup.values():
            stack.append(p)
        elif stack and stack[-1] == lookup[p]:
            stack.pop
    return stack == 0

#Driver function
print(parentheses('(())')) #True
print(parentheses2('([]')) #False
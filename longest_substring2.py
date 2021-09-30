def longest(string):
    start = 0
    end = 0
    result = 0
    dict = {}
    while end < len(string):
        c = string[end]
        if c in dict:
            start = max(start,dict[c])
        result = max(result,end-start)
        dict[string[end]] = end
        end += 1
    return result


#Driver Function
print(longest("abcabcbb")) #3
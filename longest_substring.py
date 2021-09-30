def longest_substring(string):
    dict = {}
    window_start = 0 
    window_end = 0
    result = 0  
     
    
    
    for window_end in range(len(string)):
        if string[window_end] in dict:
            window_start = max(window_start,dict[string[window_end]])
        result = max(result,window_end - window_start)
        dict[string[window_end]] = window_end
    return result

#driver
v = "abcabcbb"
 #      ^
 #   ^
print(longest_substring(v))
        
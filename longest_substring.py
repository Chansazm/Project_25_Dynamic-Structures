def longest_substring(s):
    n = len(s)
    map = {}
    window_end = 0
    result = 0  
    window_start = 0  
    
    
    for window_end in range(n):
        if s[window_end] in map:
            window_start = max(window_start,map[s[window_end]])
        result = max(result,window_end - window_start+1)
        map[s[window_end]] = window_end + 1
    return result

#driver
v = "abcabcbb"
print(longest_substring(v))
        
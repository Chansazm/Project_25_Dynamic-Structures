def longestpalindrome(s):
    if len(s) == 1: return None
    reverse = s[::-1]
    
    result = ""
    for i in s:
        print(i,s[i])
    
#Driver function
print(longestpalindrome("babad"))

def foo(s):
    n = len(s)
    table = [n*0]
    

def canconstruct(target,wordbank):
    if target == '': return True
    
    for word in wordbank:
        if target.index(word) == 0:
            suffix = target.split(word)
            if canconstruct(suffix,wordbank) == True:
                return True
    return False


#Driver function
print(canconstruct("abcdef",["ab","abc","cd","def","abcd"]))
            
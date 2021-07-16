class solution:

    def longest_palindrome(self,s):
        res = ""
        for i in range(len(s)):
            odd = self.helperpalindrome(s,i,i)
            even = self.helperpalindrome(s,i,i+1)
            res = max(odd,even,res,key=len)
        return res
        
    
    
    
    
    def helperpalindrome(self,s,l,r):
        while l >= 0 and r <= len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
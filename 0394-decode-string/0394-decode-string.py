class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s, 0)[0]

    def helper(self, s, i):
        res = ""
        num = 0
        
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])  
            
            elif s[i] == '[':
                sub, i = self.helper(s, i + 1)  # Recursively decode
                res += sub * num  
                num = 0  # Reset number
            
            elif s[i].isalpha():
                res += s[i]  
            
            else:  # ']' 
                return res, i
            
            i += 1
        
        return res, i

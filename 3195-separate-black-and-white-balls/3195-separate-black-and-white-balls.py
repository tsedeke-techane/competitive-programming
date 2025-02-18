class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)  
        min_step = 0
        left = 0 

        for right in range(len(s)):  
            if s[right] == "0":  
                if s[left] == "1": 
                    s[left], s[right] = s[right], s[left]  
                    min_step += (right - left) 
                left += 1  
        
        return min_step

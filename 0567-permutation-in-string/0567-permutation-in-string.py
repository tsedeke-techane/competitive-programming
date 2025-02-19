class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 

        s1_count = Counter(s1)  
        window_count = Counter(s2[:len(s1)]) 

        if s1_count == window_count:
            return True 

        left = 0
        for right in range(len(s1), len(s2)):
            window_count[s2[right]] += 1 
            window_count[s2[left]] -= 1 
            
            # Ensures correct dictionary comparison
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1 

            if s1_count == window_count:
                return True  

        return False 

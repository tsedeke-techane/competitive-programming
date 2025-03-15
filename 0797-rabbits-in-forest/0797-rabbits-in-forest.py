class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for rabbits, freq in count.items():
            group_size = rabbits + 1 
            groups = (freq + group_size - 1) // group_size  
            ans += groups * group_size  

        return ans


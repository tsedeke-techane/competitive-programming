class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)  
        arr = nums[:]
        for i in range(1, n):
            arr[i] += arr[i - 1]

        prefix_sum = [0] + arr
        total_sum = prefix_sum[-1]  
        
        ans = []
        for i in range(n):
            left = nums[i] * i - prefix_sum[i]  
            right = (total_sum - prefix_sum[i+1]) - nums[i] * (n - i - 1) 
            ans.append(left + right)
        
        return ans

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median_index = len(nums) // 2
        median = nums[median_index]
        ans = 0
        for num in nums:
            ans += abs(median - num)

        return ans
        
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1

        return ans

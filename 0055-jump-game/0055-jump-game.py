class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0
        for index, num in enumerate(nums):
            if index > max_reach:
                return False
            max_reach = max(max_reach, index + num)

        return True


        
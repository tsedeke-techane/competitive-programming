class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def maxScoreDifference(left, right):
            if left == right:
                return nums[left]  
        
            pickLeft = nums[left] - maxScoreDifference(left + 1, right)
            pickRight = nums[right] - maxScoreDifference(left, right - 1)

            return max(pickLeft, pickRight)
        
        return maxScoreDifference(0, len(nums) - 1) >= 0

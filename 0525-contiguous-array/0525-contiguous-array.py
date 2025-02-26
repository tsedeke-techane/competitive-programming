class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        count_map = {0 : -1}
        for index, num in enumerate(nums):
            if num == 1:
                count += 1 
            else:
                count -= 1
            if count in count_map:
                ans = max(ans, index - count_map[count])

            else:
                count_map[count] = index

        return ans
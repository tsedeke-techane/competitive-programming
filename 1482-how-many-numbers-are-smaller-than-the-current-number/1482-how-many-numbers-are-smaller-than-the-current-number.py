class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_num = sorted(nums)
        num_dict = {}
        ans = []
        for index, value in enumerate(sort_num):
            if value not in num_dict:
                num_dict[value] = index

        for num in nums:
            ans.append(num_dict[num])

        return ans




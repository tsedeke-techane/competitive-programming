class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        count_map = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                count_map[product] += 1 

        ans = 0
        for count in count_map.values():
            if count >= 2:
                ans += count * (count - 1) // 2 * 8

        return ans
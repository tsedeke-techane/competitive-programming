class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n
        ans = 0
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]

        nums.sort()
        freq.sort()

        max_total = sum(num * fr for num, fr in zip(nums, freq))
        ans = max_total % (10**9 + 7)

        return ans


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        ans = 0
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        max_total = sum(num * fr for num, fr in zip(nums, freq))

        ans = max_total % (10**9 + 7)

        return ans


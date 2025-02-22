class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        zeros = s.count("0")
        ones = n - zeros
        left_zeros = left_ones = 0
        ways = 0

        for ch in s:
            if ch == "0":
                ways += left_ones * (ones - left_ones)
                left_zeros += 1
            else:
                ways += left_zeros * (zeros - left_zeros)
                left_ones += 1

        return ways

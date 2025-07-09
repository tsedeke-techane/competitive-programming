class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for fact in range(1, min(a, b) + 1):
            if a % fact == 0 and b % fact == 0:
                ans += 1

        return ans
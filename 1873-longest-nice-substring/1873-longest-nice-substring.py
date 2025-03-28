class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        s_set = set(s)
        for i, char in  enumerate(s):
            if char.swapcase() not in s_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1 :])

                return right if len(right) > len(left) else left

        return s

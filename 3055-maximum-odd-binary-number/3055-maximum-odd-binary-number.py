class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        ans = [0] * len(s)
        ans[-1] = 1
        for i in range(count['1'] - 1):
            ans[i] = 1

        return ''.join(map(str, ans))
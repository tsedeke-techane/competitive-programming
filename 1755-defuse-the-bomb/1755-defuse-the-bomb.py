class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        # Duplicate the array for circular behavior
        extended = code + code

        # Build prefix sum
        prefix = [0] * (len(extended) + 1)
        for i in range(len(extended)):
            prefix[i + 1] = prefix[i] + extended[i]

        if k > 0:
            for i in range(n):
                ans[i] = prefix[i + k + 1] - prefix[i + 1]
        else:
            k = -k
            for i in range(n):
                ans[i] = prefix[i + n] - prefix[i + n - k]

        return ans

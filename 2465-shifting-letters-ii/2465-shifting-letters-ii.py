class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_arr = [0] * (n + 1)

        # Update prefix array based on shifts
        for start, end, direction in shifts:
            if direction == 1:
                value = 1
            else:
                value = -1

            prefix_arr[start] += value
            prefix_arr[end + 1] -= value

        # Compute prefix sum
        for i in range(1, n):
            prefix_arr[i] += prefix_arr[i - 1]

        ans = []
        for i in range(n):
            new_char = chr(ord('a') + (ord(s[i]) - ord('a') + prefix_arr[i]) % 26)
            ans.append(new_char)

        return ''.join(ans)
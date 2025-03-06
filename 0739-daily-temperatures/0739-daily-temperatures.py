class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for cur_idx in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[cur_idx]:
                prev_idx = stack.pop()
                ans[prev_idx] = cur_idx - prev_idx

            stack.append(cur_idx)
        return ans
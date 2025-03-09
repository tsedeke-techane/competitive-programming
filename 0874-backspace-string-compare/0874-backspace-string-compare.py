class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for val in s:
            if s[0] == '#':
                continue

            if val == '#':
                if stack_s:
                    stack_s.pop()
                else:
                    continue

            else:
                stack_s.append(val)

        for val in t:
            if val == '#':
                if stack_t:
                    stack_t.pop()
                else:
                    continue

            else:
                stack_t.append(val)

        return stack_t == stack_s
                 
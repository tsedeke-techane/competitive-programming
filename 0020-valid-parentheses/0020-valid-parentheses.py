class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {'(':')', '{':'}', '[':']'}
        for charr in s:
            if charr in '({[':
                stack.append(charr)
            else:
                if not stack:
                    return False 
                elem = stack.pop()
                if mp[elem] != charr:
                    return False

        return not stack


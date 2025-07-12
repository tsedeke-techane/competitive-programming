class Solution:
    def freqAlphabets(self, s: str) -> str:
        def helper(s):
            return chr( 97 + int(s) - 1) 

        i = 0
        n = len(s)
        ans = []
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                decode = helper(s[i : i + 2])
                ans.append(decode)
                i += 3

            else:
                ans.append(helper(s[i]))
                i += 1

        return ''.join(ans)

            




        

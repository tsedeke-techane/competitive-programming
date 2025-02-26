class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i

        print(lastIdx)
        
        curLast = 0
        curStart = 0
        ans = []
        for i in range(len(s)):
            curLast = max(curLast, lastIdx[s[i]])
            if i == curLast:
                ans.append(curLast - curStart + 1)
                curStart = i + 1
        
        return ans
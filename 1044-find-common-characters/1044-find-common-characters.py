import collections
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        result = []

        common_cnt = collections.Counter(words[0])  # counts for first word

        for i in range(1, n):
            curr_cnt = collections.Counter(words[i])  # counts for current word

            for ch in common_cnt.keys():
                common_cnt[ch] = min(common_cnt[ch], curr_cnt[ch])

        for ch, cnt in common_cnt.items():
            result.extend([ch] * cnt)

        return result

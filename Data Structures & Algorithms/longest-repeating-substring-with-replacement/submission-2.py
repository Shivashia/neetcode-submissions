
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = defaultdict(int)
        max_len = 0

        l = 0
        r = 0

        while r < len(s):
            # Add current character to window
            res[s[r]] += 1

            win_len = r - l + 1
            max_freq = max(res.values())

            # Shrink until window becomes valid
            while win_len - max_freq > k:
                res[s[l]] -= 1
                l += 1

                win_len = r - l + 1
                max_freq = max(res.values())

            max_len = max(max_len, win_len)
            r += 1

        return max_len

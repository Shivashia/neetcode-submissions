class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_1 = defaultdict(int)

        for ch in t:
            freq_1[ch] += 1

        freq_2 = defaultdict(int)

        required = len(freq_1)
        formed = 0

        l = 0
        min_len = float('inf')
        res = ""

        for r in range(len(s)):
            freq_2[s[r]] += 1

            # Did this character just reach its required frequency?
            if s[r] in freq_1 and freq_2[s[r]] == freq_1[s[r]]:
                formed += 1

            # Window is valid when all requirements are satisfied
            while formed == required:
                window_len = r - l + 1

                if window_len < min_len:
                    min_len = window_len
                    res = s[l:r+1]

                # Remove the leftmost character
                freq_2[s[l]] -= 1

                # Did removing it break a satisfied requirement?
                if s[l] in freq_1 and freq_2[s[l]] < freq_1[s[l]]:
                    formed -= 1

                l += 1

        return (res)
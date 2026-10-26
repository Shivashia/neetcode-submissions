class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_map_base = defaultdict(int)

        for ch in s1:
            freq_map_base[ch] += 1

        window = len(s1)
        l = 0
        r = 0
        freq_map = defaultdict(int)

        while r < len(s2):
            freq_map[s2[r]] += 1

            if r - l + 1 > window:
                freq_map[s2[l]] -= 1

                if freq_map[s2[l]] == 0:
                    del freq_map[s2[l]]

                l += 1

            if r - l + 1 == window:
                if freq_map_base == freq_map:
                    return True

            r += 1

        return False
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 
        for r in range(len(s)):
            l = r
            temp = k
            while l < len(s) and temp > 0:
                if s[l] == s[r]:
                    l+=1
                else:
                    temp-=1
                    l+=1
            max_len = max(max_len, l-r+1)

        return (max_len)
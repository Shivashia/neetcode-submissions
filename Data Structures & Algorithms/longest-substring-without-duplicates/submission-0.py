class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            res = set()
            res.add(s[i])
            j=i+1
            while (j < len(s)):
                # print(res,s[j])
                if s[j] not in res:
                    res.add(s[j])
                    j+=1
                else:
                    break
            max_len = max(max_len, len(res))
        return max_len
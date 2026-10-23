class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1

            res.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         for i in range(len(s)):
#             res = set()
#             res.add(s[i])
#             j=i+1
#             while (j < len(s)):
#                 # print(res,s[j])
#                 if s[j] not in res:
#                     res.add(s[j])
#                     j+=1
#                 else:
#                     break
#             max_len = max(max_len, len(res))
#         return max_len
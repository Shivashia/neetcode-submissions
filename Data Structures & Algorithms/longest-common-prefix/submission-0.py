class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1=strs[0]
        for i in strs[1:]:
            ind=0
            for j in range(len(i)):
                if j<len(s1) and s1[j] == i[j]:
                    ind=j+1
                else:
                    break
            s1=s1[:ind]

            if s1 == "":
                return ""
        return s1


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            dict_ans={}
            for i in s:
                if i in dict_ans.keys():
                    dict_ans[i]+=1
                else:
                    dict_ans[i]=1
            for j in t:
                if j in dict_ans.keys():
                    dict_ans[j]-=1
                else:
                    dict_ans[j]=1
            for i in dict_ans.values():
                if i != 0:
                    return False
            return True

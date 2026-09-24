class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i]+=1
        res=[]
        for key,value in hm.items():
            res.append([key,value])
        # print(res)
        res.sort(key = lambda x:x[1])
        # print(res)
        fin=[]
        i=0
        while i < k:
        # print(len(res)-i-1)
            fin.append(res[len(res)-i-1][0])
            i+=1
        return fin
        # print(fin)
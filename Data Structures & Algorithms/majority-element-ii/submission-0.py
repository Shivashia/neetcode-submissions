class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        qual=len(nums)//3
        res=[]
        st = set()
        for i in nums:
            hm[i]+=1
            if hm[i] > qual:
                st.add(i)
        return list(st)
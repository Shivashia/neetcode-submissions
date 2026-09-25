class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set()
        for i in nums:
            hs.add(i)

        max_len=0;
        for i in hs:
            if i-1 not in hs:
                curr_len=1
                while i+1 in hs:
                    curr_len+=1
                    i+=1
                max_len = max(max_len,curr_len)
        return max_len
       

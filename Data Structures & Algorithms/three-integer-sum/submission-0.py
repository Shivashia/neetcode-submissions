class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            j=i+1
            k =len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j<k:
                tot= nums[i]+nums[j]+nums[k]
                if tot == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif tot<=0:
                    j+=1
                else:
                    k-=1
            
        return res
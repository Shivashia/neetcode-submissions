class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        z_cnt=0
        for i in nums:
            if i!=0:
                prod*=i
            else:
                z_cnt+=1
        if z_cnt>1:
            return  [0]*len(nums)

        for i in range(len(nums)):
            if z_cnt==1 :
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=prod
            else:
                nums[i]=int(prod/nums[i])
        return nums
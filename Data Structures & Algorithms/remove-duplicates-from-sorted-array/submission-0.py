class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=0
        r=0
        while r<len(nums):
            if nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
            r+=1
        return l+1
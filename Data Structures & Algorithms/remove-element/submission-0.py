class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1,p2=0,len(nums)-1
        while p1<p2:
            if nums[p2]==val:
                p2-=1
            elif nums[p1]==val and nums[p2]!=val:
                nums[p1],nums[p2]=nums[p2],nums[p1]
            else:
                p1+=1
        return p2+1

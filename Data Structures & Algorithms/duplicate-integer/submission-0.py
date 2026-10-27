class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for num in nums:
            if nums in s:
                return True
            s.add(num)
        return False
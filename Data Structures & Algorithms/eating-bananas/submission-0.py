class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cnter(nums, speed):
            tot=0
            for i in nums:
                tot+=math.ceil(i/speed)
            return tot
        start= min(piles)
        end = max(piles)
        min_speed=start
        while start<=end:
            mid = start + (end-start)//2
            if cnter(piles,mid) <= h:
                min_speed = max(min_speed,mid)
                end = mid-1
            else:
                start = mid+1
        return min_speed

        # print(cnter(piles,2))
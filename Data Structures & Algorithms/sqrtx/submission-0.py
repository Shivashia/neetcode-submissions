class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end = x
        while start<=end:
            mid = start +(end-start)//2
            tmp = mid*mid
            if tmp > x:
                end = mid-1
            elif tmp < x:
                start = mid+1
            else:
                return mid
        return end 
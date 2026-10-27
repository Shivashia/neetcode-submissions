class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)-1
        max_vol=0

        for i in range(n,-1,-1):
            for j in range(i-1,-1,-1):
                max_vol=max(max_vol,min(heights[i],heights[j])*(i-j))
        return max_vol
        
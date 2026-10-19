class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bnSearch(nums, start,end):
            print(nums, start, end)
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start= mid +1
                else:
                    return True
            return False

        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                return bnSearch(matrix[i],0,len(matrix[i])-1)
        return False

        
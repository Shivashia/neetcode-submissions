class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculateDays(weights, capacity):
            days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight <= capacity:
                    current_load += weight
                else:
                    days += 1
                    current_load = weight

            return days

        start = max(weights)
        end = sum(weights)
        min_capacity = end 

        while start <= end:
            mid = start + (end - start) // 2

            if calculateDays(weights, mid) <= days:
                min_capacity = min(min_capacity, mid)
                end = mid - 1
            else:
                start = mid + 1

        return min_capacity
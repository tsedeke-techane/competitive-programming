class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        if len(nums) == 2:
            return min(cost) * abs(nums[0] - nums[1])

        pair = sorted(zip(nums, cost))   
        median_freq = sum(cost) // 2
        frequency = 0
        median = 0
        
        for num, cost in pair:
            frequency += cost
            median = num
            if frequency >= median_freq:
                break

        total_cost = 0
        for num, cost in pair:
            total_cost += abs(num - median) * cost

        return total_cost

            


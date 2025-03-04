class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        n = len(costs) // 2
        ans = 0
        
        for i in range(n):
            ans += costs[i][0]

        for i in range(n):
            ans += costs[n + i][1]                              

        return ans
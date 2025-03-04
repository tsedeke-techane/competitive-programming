class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost:  cost[1]- cost[0])
        n = len(costs) // 2
        ans = sum(cost[0] for cost in costs)
        
        for i in range(n):
            ans -= costs[i][0]
            ans += costs[i][1]
        return ans
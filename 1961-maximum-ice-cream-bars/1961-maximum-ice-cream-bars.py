class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        num_ice = 0
        for cost in costs:
            if coins < cost:
                return num_ice

            coins -= cost
            num_ice += 1

        return num_ice
        
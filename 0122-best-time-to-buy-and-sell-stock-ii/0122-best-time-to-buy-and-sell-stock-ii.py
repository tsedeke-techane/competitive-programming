class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = price - buy_price
                max_profit += profit
                buy_price = price

        return max_profit
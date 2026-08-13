class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit, profit = 0, 0
        left, right = 0, 1 

        while right < len(prices):
            if prices[right] - prices[left] <= 0:
                left += 1
                right += 1

            else:
                cur_profit = prices[right] - prices[left]
                profit = max(cur_profit, profit)
                right += 1

        return profit
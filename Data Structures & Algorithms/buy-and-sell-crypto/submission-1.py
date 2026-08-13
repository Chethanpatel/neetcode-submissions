class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1 

        while right < len(prices):
            if prices[left] < prices[right]:
                cur_profit = prices[right] - prices[left]
                profit = max(cur_profit, profit)
            else:
                left = right
            
            right += 1
        return profit
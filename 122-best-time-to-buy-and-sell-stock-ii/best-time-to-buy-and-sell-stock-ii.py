class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy=prices[0]
        for sell in prices[1:]:
            if sell>buy:
                max_profit+=sell-buy
            buy=sell
        return max_profit
        
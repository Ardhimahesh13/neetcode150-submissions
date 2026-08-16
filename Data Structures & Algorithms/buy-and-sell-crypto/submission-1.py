class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = float('inf')
        max_profit    = 0
        
        for price in prices :
            if price < min_buy_price :
                min_buy_price = price
            elif price - min_buy_price > max_profit :
                max_profit = price - min_buy_price
        return max_profit

        
        
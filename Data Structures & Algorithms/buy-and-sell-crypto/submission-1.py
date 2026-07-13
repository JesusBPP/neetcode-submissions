class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        rigth = 1
        profit = 0
        cambio = False
        while rigth < len(prices):
            cambio = False
            if (prices[rigth] - prices[left]) > profit:
                profit = prices[rigth] - prices[left]
            elif (prices[rigth] - prices[left]) < 0:
                left = rigth
                if rigth < len(prices):
                    cambio = True
                    rigth += 1
            if cambio == False:
                rigth += 1
        
        return profit
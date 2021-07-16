def maxProfit(prices):
        maximum_profit = 0
        for buy in range(len(prices)):
            for sale in range(buy,len(prices)):
                maximum_profit = max(maximum_profit,prices[sale]-prices[buy])
        return maximum_profit
    
print(maxProfit([9, 11, 8, 5, 7, 10]))
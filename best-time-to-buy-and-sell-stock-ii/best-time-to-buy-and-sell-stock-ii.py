class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Start with a buy price of prices[0]
        #Keep track of profits = 0
        #Go through prices one by one
            #If the price im at now is lower 
                #Make this the buy price
            #If the price is higher 
                #Add the difference to profits, make this the buy price
        buyPrice = prices[0]
        profits = 0
        for price in prices[1:]:
            if price < buyPrice:
                buyPrice = price
            else:
                profits += price - buyPrice
                buyPrice = price
        return profits
                
            
            
            
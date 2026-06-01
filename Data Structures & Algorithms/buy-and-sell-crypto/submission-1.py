class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #buying
        right = 1 #selling
        maxProf = 0 #our max profit is zero because we haven't gotten anything

        while right < len(prices): #we continue iterating our prices and dont want
        #it to go out of bounds
            if prices[left] < prices[right]: #checking if it is the lowest time to buy and highest time to sell
                tmp = prices[right] - prices[left]
                if tmp > maxProf: #need to check if its our max profit
                    maxProf = tmp
                right+=1 #incrementing our right to see any other profits
            else:
                left = right #this is the scenario when right is lower than the left,
                #in this case we make left become right so it is the lowest
                right+=1 #incrementing right to find the next max
        return maxProf

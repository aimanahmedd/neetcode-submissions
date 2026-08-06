class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand
        input: integer array prices
        output: the best day to buy and sell stock

        [10, 1, 5, 6, 7, 1]

        buy low sell high!

        buy first, sell after

        match:
            use sliding window -> keep track of what to buy and sell in the future

        plan:
        1. make a pointer on left (buy), right(sell), and maxprofit= 0
        2. while right < len(prices):
            if prices[right] < prices[left]: -> try while loop here
                left = right
                right +=1
            
            maxProfit = max(prices[right]-prices[left], maxProfit)

            right +=1

        3. return maxProfit
        '''
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            while prices[right] < prices[left] and right < len(prices)-1:
                left = right
                right +=1

            maxProfit = max(prices[right]-prices[left], maxProfit)

            right+=1
        return maxProfit
        
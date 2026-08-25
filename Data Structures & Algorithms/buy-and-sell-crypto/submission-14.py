class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: integer array prices, prices[i] is the price of neetcoin on ith day
        output: max profit we can achieve

        [10, 1, 5, 6, 7, 1]
        -> 6
        buy prices[1] = 1 (cheap) and sell prices[4] = 7 (big bucks)

        prices will always have at least one day

        prices[i] range betweem 0 and 100

        match:
            sliding window to keep track what we buy and what we sell in the 
            future and to continue going along on the window

        plan:
        1. create a left and right pointer to point to the first element in the array
        2. create maxProfit variable equal to 0 to represnet our profit
        3. while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
                right+=1
            else:
                left = right
                right+=1
        4. return maxProfit
        '''
        left, right = 0, 0
        maxProfit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right]-prices[left]
                maxProfit = max(maxProfit, profit)
                right+=1
            else:
                left = right
                right+=1
        return maxProfit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: price array where i in the price of neetcoin on ith day
        output: max profit

        [10, 1, 5, 6 7,, 1]
        -> 6
        
        [10, 8, 7, 5, 2]
        ->0 all are more cheaper at the end we would not make a lot of money

        prices will always have at least one price on a day and up to 100
        between 0 and 100

        match:
            sliding window because pointers can be the same :)

        plan:
            1. set maxProfit variable = 0
            2. create a left pointer (represent buy) and right pointer (represent sell) equal to first index
            3. while right >= left:
                prof = prices[right] - prices[left]

                maxProfit = max(maxProfit, prof)
                left = right
                right+=1

        '''
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right] - prices[left])
            else:
                left = right
            right+=1
        return maxProf




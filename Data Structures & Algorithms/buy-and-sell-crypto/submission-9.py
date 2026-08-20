class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: prices array, prices i is the price for ith day
        output: max profit attainable

        [10, 1, 5, 6, 7, 1]
        -> max profit would be 6 because we buy on prices[1] and sell prices[74]
                7-1 = 6
        match:
            sliding window to be able to keep track of max right min left
        plan:
        1. left and right pointer, left = 0 right points to 1 (second index)
        2. max profit = 0 (default case)
        3. while right > len(prices) only movign right to find the highest price
        we can selld:
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right]-prices[left])
            else:
                left = right
            right+=1 we dont move up left, because if we found its already cheaper
            to buy we dont need to move it
        '''
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right] -prices[left])
            else:
                left = right

            right+=1

        return maxProf
        
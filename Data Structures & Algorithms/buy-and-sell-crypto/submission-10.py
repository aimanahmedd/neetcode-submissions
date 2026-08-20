class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: integer array of prices ith day is the price
        output: max profit attainable

        [10, 1, 5, 6, 7, 1]
        6
        buy on prices[1] and sell prices[7]

        we always want to buy first and then sell after we bought
        we need to buy something cheap and sell expensice

        there can be a case with 0 profit -> all future days are too expensive
        or only element

        match:
            sliding window to keep track of min sell and max buy

        plan:
        1. left, right = 0, 1
        2. maxProf
        3. while right < len(prices):
            if prices[right] > prices[left]:
                prof = prices[right] - prices[left]

                maxProf = max(maxProf, prof)
            else:
                left = right
            right+=1
        4. return maxProf

            [5, 3, 14, 2]

        '''
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                prof = prices[right] - prices[left]

                maxProf = max(maxProf, prof)
            else:
                left = right
            right+=1
        return maxProf
        
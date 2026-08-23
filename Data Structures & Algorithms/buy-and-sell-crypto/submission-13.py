class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: integer array prices, where prices[i] = price on ith day
        output: max profit from buying and selling

        buying must be done in the past, selling in the futre

        [10, 1, 5, 6, 7, 1]
        -> 6
        buy on price[1] = 1 (cheap) sell on princes[4] = 7 (expensive)!
        7-1 = 6

        there may be a day where profit is 0

        [10, 8, 7, 5, 2]
        -> 0 because no day in the futrue is good to sell

        prices length between 1 and 100
        there can be 0 to 100 dollars

        [10, 10, 10] -> no profitable trans

        match:
            sliding window to keep track of the future on what a good transaction
            would be
        
        plan:
        1. make left and right pointer, left representing buying and right
        representing selling. both pointing to first element in array
        2. maxProf = 0
        3. while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right]-prices[left])
                right+=1
            else:
                left = right
                right+=1
        4. return maxProf
        '''
        left, right = 0, 0
        maxProf = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right]-prices[left])
                right+=1
            else:
                left = right
                right+=1
        return maxProf
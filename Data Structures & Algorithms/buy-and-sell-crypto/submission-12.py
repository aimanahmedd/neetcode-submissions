class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
        input: integer array of prices where price i is the price of ith day
        output: max profit we can make from buying and selling

        [10, 1, 5, 6, 7, 1]
        -> buy on prices[1] = 1 (cheapest) sell on prices[4] = 7 (expensive)

        there can be cases where we make 0 profit!

        [10, 8, 7, 5, 2]
        -> no cases where it is cheaper to buy first

        always have at least one element in array: doesnt mean we will 
        necessarily buy and sell :p

        match:
            consider a point in the future and keep expanding on future element
            values
                
        plan:
        1. making a left pointer first element (buying) and right pointer second 
        element (selling)
        2. make an empty var for maxprof
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
                left=right
                right+=1
        return maxProf
        
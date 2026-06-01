class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProf = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                tmp = prices[right] - prices[left]
                if tmp > maxProf:
                    maxProf = tmp
                    right+=1
                else:
                    right+=1
            else:
                left = right
                right+=1
            #right+=1
        return maxProf

'''
Solution in words:
what i essentially did was create a left pointer and a right pointer directly ahead of it.
basically our goal is to find lowest price that we can buy which is left, and the highest
price we can sell, which is left. so while our right is still in the range of the list, because 
we are always incrementing our right, we check if the price of the left is smaller
than the price of the right. if it is, we can calculate it by subtracting right price to
get left price, and if that is greater than the current max profit, we update the max profit.
else we increment the left pointer to become right (since this is the scenario where right is the lowest)
and increment right to be one more ahead. outside the while loop we return the max profit!:)
'''
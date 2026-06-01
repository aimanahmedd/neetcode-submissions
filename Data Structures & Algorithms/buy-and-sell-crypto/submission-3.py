class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =  0
        right = 1
        maxProf = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                tmp = prices[right]-prices[left]
                if tmp > maxProf:
                    maxProf = tmp
                right+=1
            else:
                left = right

                right+=1
        return maxProf

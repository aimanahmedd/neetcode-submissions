class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        understsnd:
        input: integer array prices
        output: profit from buying and selling
        [10, 1, 5, 6, 7, 1]
        7-1 = 6
        7 most expensive to sell
        1 is most cheap to buy

        match:
            sliding windoe to keep track what ahead to buy and sell

        plan:
        1. create a variable to buy, sell, to represent inde an
        d profit
        2. while right is great than the length of array:
         if price of right is greater than price of left
         calculate profit

         if that profit grater than current prift make new profit
         else move up right

        """
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                tmp = prices[sell] - prices[buy]

                if tmp > profit:
                    profit = tmp
                sell += 1
            else:
                buy = sell
                sell += 1

        return profit

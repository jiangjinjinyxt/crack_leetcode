"""
problem 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

solution:

""" 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre_min = float('inf')
        maximum = 0
        for price in prices:
            if price < pre_min:
                pre_min = price
            elif price > pre_min:
                if price - pre_min > maximum:
                    maximum = price - pre_min
        return maximum
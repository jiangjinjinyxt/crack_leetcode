"""
problem 121. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

solution:

""" 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre_min = float('inf')
        profit = 0
        for price in prices:
            if price < pre_min:
                pre_min = price
            elif price > pre_min:
                profit += price - pre_min
                pre_min = price
        return profit
"""
problem 134. Gas Station
https://leetcode.com/problems/gas-station/

solution:

""" 

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        min_index = -1
        min_amount = 0
        total_amount = 0
        for index in range(len(gas)):
            total_amount += gas[index] - cost[index]
            if total_amount < min_amount:
                min_amount = total_amount
                min_index = index
        if total_amount < 0:
            return -1
        else:
            return min_index + 1 if min_index < len(gas) - 1 else 0


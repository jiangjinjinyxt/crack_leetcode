"""
problem 119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

solution:

""" 

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pre = [1]
        pre_len = 1
        for i in range(rowIndex):
            pre_len += 1
            cur = [1] * pre_len
            for idx in range(1, pre_len - 1):
                cur[idx] = pre[idx - 1] + pre[idx]
            pre = cur
        return pre

"""
problem 60: Permutation Sequence
https://leetcode.com/problems/permutation-sequence/

solution:

""" 
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        table = list(range(1, n + 1))
        result = ""
        while n:
            fac //= n
            index = (k - 1) // fac
            k %= fac
            n -= 1
            
            result += str(table[index])
            table.pop(index)
        return result
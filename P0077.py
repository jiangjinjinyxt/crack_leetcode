"""
problem 77: Combinations
https://leetcode.com/combinations/

solution:

""" 
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        table = list(range(1, n + 1))
        result = []
        if k > n:
            return result
        if k == n:
            return [table]

        def helper(index, nums, ans):
            if nums == 0:
                result.append(ans.copy())
            else:
                if n - index >= nums:
                    for idx in range(index, n - nums + 1):
                        ans.append(table[idx])
                        helper(idx + 1, nums - 1, ans)
                        ans.pop()
        helper(0, k, [])
        return result


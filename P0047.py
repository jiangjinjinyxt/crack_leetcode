"""
problem 47: Permutations II
https://leetcode.com/problems/permutations-ii/

solution:

""" 
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        table = dict()
        used = dict()
        for num in nums:
            if num not in table:
                table[num] = 0
                used[num] = 0
            table[num] += 1
        length = len(nums)
        result = []

        def helper(ans):
            if len(ans) == length:
                result.append(ans.copy())
            else:
                for num, total in table.items():
                    if used[num] < total:
                        ans.append(num)
                        used[num] += 1
                        helper(ans)
                        ans.pop()
                        used[num] -= 1
        helper([])
        return result
"""
problem 46: Permutations
https://leetcode.com/problems/permutations/

solution:

""" 
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            return [[value] + i for idx, value in enumerate(nums) for i in self.permute(nums[:idx] + nums[idx+1:])]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        result = []

        def helper(ans):
            if len(ans) == length:
                result.append(ans.copy())
            else:
                for value in nums:
                    if value not in ans:
                        ans.append(value)
                        helper(ans)
                        ans.pop()
        helper([])
        return result
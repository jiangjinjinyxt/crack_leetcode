"""
problem 39: Combination Sum
https://leetcode.com/problems/combination-sum/

solution:

""" 
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        length = len(candidates)
        table = dict()

        def helper(target, left_index):
            if (target, left_index) in table:
                return table[(target, left_index)]
            result = []
            for index in range(left_index, length):
                if candidates[index] > target:
                    break
                elif candidates[index] == target:
                    result.append([target])
                else:
                    result.extend([[candidates[index]] + i for i in helper(target - candidates[index], index)])
            table[(target, left_index)] = result
            return result
        return helper(target, 0)


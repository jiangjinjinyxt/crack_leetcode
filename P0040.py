"""
problem 40: Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

solution:

""" 
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(candidates)
        candidates.sort()

        def helper(target, left_index):
            if left_index >= length:
                return []
            previous = candidates[left_index]
            if previous > target:
                return []
            elif previous == target:
                return [[target]]
            else:
                count = 1
                for index in range(left_index + 1, length):
                    if candidates[index] == previous:
                        count += 1
                    else:
                        break
                else:
                    if (not target % previous) and (target // previous <= count):
                        return [[previous] * (target // previous)]
                    else:
                        return []
                result = []
                for i in range(min(target // previous, count) + 1):
                    if i * previous == target:
                        result.extend([[previous] * i])
                    else:
                        result.extend([[previous] * i + j for j in helper(target - previous * i, index)])
                return result
        return helper(target, 0)


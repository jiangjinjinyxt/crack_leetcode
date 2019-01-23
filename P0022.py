"""
problem 22: Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

solution:
    https://leetcode.com/problems/generate-parentheses/solution/

"""  

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(left, right):
            if left < n:
                if left > right:
                    return [')' + _ for _ in helper(left, right + 1)] + ['(' + _ for _ in helper(left + 1, right)]
                else:
                    return ['(' + _ for _ in helper(left + 1, right)]
            elif left == n:
                if left > right:
                    return [')' + _ for _ in helper(left, right + 1)]
                else:
                    return [""]
        return helper(0, 0)


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def back_track(previous="", left=0, right=0):
            if len(previous) == 2 * n:
                result.append(previous)
            else:
                if left < n:
                    back_track(previous+'(', left+1, right)
                if right < left:
                    back_track(previous+')', left, right+1)
        back_track()
        return result
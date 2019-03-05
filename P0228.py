"""
Problem 228. Summary Ranges
https://leetcode.com/problems/summary-ranges/

solution:

"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if not nums:
            return ans
        start = end = nums[0]
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append("{}->{}".format(start, end))
                start = num
                end = num
        if start == end:
            ans.append(str(start))
        else:
            ans.append("{}->{}".format(start, end))
        return ans
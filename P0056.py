"""
problem 56: Merge Intervals
https://leetcode.com/problems/merge-intervals/

solution:

""" 
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        if len(intervals) < 2:
            return intervals

        result = []
        previous = intervals[0]
        for current in intervals[1:]:
            if current.start <= previous.end:
                if previous.end < current.end:
                    previous.end = current.end
            else:
                result.append(previous)
                previous = current
        result.append(previous)
        return result

"""
problem 57: Insert Interval
https://leetcode.com/problems/insert-interval/

solution:

""" 
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        result = []
        length = len(intervals)
        for idx, value in enumerate(intervals):
            if value.end < newInterval.start:
                result.append(value)
            elif value.start > newInterval.end:
                result.append(newInterval)
                result.append(value)
                break
            else:
                newInterval.start = min(newInterval.start, value.start)
                newInterval.end = max(newInterval.end, value.end)
        else:
            result.append(newInterval)
            return result
        for value in intervals[idx + 1:]:
            result.append(value)
        return result

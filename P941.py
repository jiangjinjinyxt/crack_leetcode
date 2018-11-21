"""
problem 941: valid mountain array
https://leetcode.com/problems/valid-mountain-array/description/

solution:
	1.  if the length of the given array is smaller than 3, 
			return False
	2.  loop through the array, use a counter to record the 
		current index.
		firstly, counting the ascending series
			while the current value is not the last value of
			the array, and the current value is smaller than
			the next value
				increase the counter by 1.
		out of the first loop, check
			if the counter is 0, means second value is not bigger
			than the first value;
			or the counter is at the last_index, means the entire
			arrary is an strictly ascending array
				return False
			else
				into the next loop
		secondly, counting the descending series
			till now, the previous series is an ascending series
			while the current value is not the last value of 
			the array, and the current value is bigger than the
			next value
				increase the counter by 1.
		out of the second loop, check
			if the counter is not equal to the last index, means 
			the next value is not less than the value at the counter
				return False
			else
				return True

"""
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length < 3:
            return False
        # index as a counter
        index = 0
        last_index = length - 1
        # first loop
        while index < last_index and A[index] < A[index + 1]:
            index += 1
        # out of first loop, check
        if index == 0 or index == last_index:
        	return False
       	# second loop
        while index < last_index and A[index] > A[index + 1]:
        	index += 1
       	# out of second loop, check
        if index == last_index:
        	return True
        else:
        	return False

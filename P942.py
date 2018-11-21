"""
problem 942: DI String Match
https://leetcode.com/problems/di-string-match/description/

solution
	firstly
		initialize the return array as an ascending series.
	secondly
		loop through the input array, use a counter to record the first 
		appearance of the previously continuous 'D's.
		initialize the counter as None,
		if current value is 'D'
			if counter is None
				means the previous value is 'I'
				counter = current index
			if counter is not None
"""

class Solution(object):
	result = None
	def diStringMatch(self, S):
		"""
		:type S: str
		:rtype: List[int]
		"""
		length = len(S)
		self.result = list(range(length + 1))
		index_of_first_D = None
		for idx, value in enumerate(S):
			if value == 'D':
				if index_of_first_D is None:
					index_of_first_D = idx
			else:
				if index_of_first_D is not None:
					self.swap_elements(index_of_first_D, idx)
					index_of_first_D = None
		if value == 'D':
			if index_of_first_D is not None:
				self.swap_elements(index_of_first_D, idx + 1)
		return self.result
	def swap_elements(self, start, end):
		print("previous: {}".format(self.result))
		if start != 0:
			self.result[start:end+1] = self.result[end:start-1:-1]
		else:
			self.result[:end+1] = self.result[end::-1]
		print("after: {}".format(self.result))
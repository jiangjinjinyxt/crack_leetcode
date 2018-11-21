"""
problem 944: Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/description

solution
	just iterate through columns
		in each column, if not in ascending order
"""

class Solution(object):
	def minDeletionSize(self, A):
		"""
		:type A: List[str]
		:rtype: int
		"""
		rows = len(A)
		if rows < 2:
			return 0
		columns = len(A[0])

		counter = 0
		for i in range(columns):
			for j in range(1, rows):
				if A[j][i] >= A[j-1][i]:
					continue
				else:
					counter += 1
					break
		return counter

"""
problem 977: Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

solution:
    

"""  

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        length = len(A)

        left_index = 0
        right_index = length - 1
        output_array = [0] * length

        negative_flag = False
        positive_flag = False

        for index in range(length - 1, -1, -1):
            if negative_flag:
                output_array[index] = A[left_index] ** 2
                left_index += 1
            elif positive_flag:
                output_array[index] = A[right_index] ** 2
                right_index -= 1
            else:
                if A[left_index] >= 0:
                    positive_flag = True
                    output_array[index] = A[right_index] ** 2
                    right_index -= 1
                elif A[right_index] <= 0:
                    negative_flag = True
                    output_array[index] = A[left_index] ** 2
                    left_index += 1
                else:
                    if - A[left_index] > A[right_index]:
                        output_array[index] = A[left_index] ** 2
                        left_index += 1
                    else:
                        output_array[index] = A[right_index] ** 2
                        right_index -= 1
        return output_array
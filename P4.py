"""
problem 4: Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

solution:
    Under explaination, we suppose the indice starts with 1.
    First: locate the median.
        Suppose we merge the two sorted arrays,
          if length of the merged array is even, then median
            is the average of the two indices(start from 1): 
            (length//2) and (length//2 + 1), like mean of (2,3)
            of an array with length 4, notice (length//2) equals
            to (length + 1)//2 when length is even.

          if length of the merged array is odd, then median 
            is at the indice(start from 1): (length//2 + 1), which 
            is the same as (length + 1)//2.

          So, no matter how long the merged array, we can always
          get the median by averaging the value at the two indices:
          (length//2) and (length//2 + 1).

    Second, we create a function two find the kth largest value of 
        the two given arrays.
        (1) if k if smaller than 0 or bigger than the length of the 
            merged array, the indice is out of range, so the function
            returns None.
        (2) if one of the sorted array is empty, just return the kth 
            largest value in the other array.
        (3) if k is equal to 1, return minimum value of the two first
            value in the two sorted arrays.
        (4)
            we take the indice of array1 at k//2, represented by index1,
            and the indice of array2 at k - k//2, represented by index2,
            so index1 + index2 == k.
            if array1[index1] >= array2[index2]:
                if array1[index1] <= array2[index2 + 1]:
                    means array1[index1] is the kth largest value.
                    because it is greater than (index1 - 1) values in 
                    array1, and greater than (index2) values in array2.
                if array1[index1] > array2[index2 + 1]:
                    means array1[index1] is greater than the kth largest value,
                    because it is greater than (index1 - 1) values in
                    array1, and greater than (index2 + 1) values in 
                    array2.
                    So array1[index1:] is useless
                    Also, as array2[index2] is at most greater than k - 2
                    (index1 - 1 in array1, index2 - 1 in array2) values in the 
                    merged array, so array2[:index2+1] is useless.
                    so we recursively find the (k - index2)th largest value 
                    in array1[:index1] and array2[index2+1:].
            else:
                same analysis as the previous situation.
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
        if len2 == 0:
            # or raise ValueError
            return None
        idxmin = 0
        idxmax = len1
        total_len = (len1 + len2 + 1) // 2
        while idxmin <= idxmax:
            index1 = idxmin + (idxmax - idxmin) // 2
            index2 = total_len - index1
            if index1 > 0 and nums1[index1 - 1] > nums2[index2]:
                # index1 too big
                idxmax = index1 - 1
            elif index1 < m and nums2[index2 - 1] > nums1[index1]:
                # index1 too small
                idxmin = index1 + 1
            else:
                # perfect
                if index1 == 0:
                    left_max = nums2[index2 - 1]
                elif index2 == 0:
                    left_max = nums1[index1 - 1]
                else:
                    left_max = max(nums1[index1 - 1], nums2[index2 - 1])

                if (len1 + len2) % 2:
                    return left_max

                if index1 == len1:
                    right_min = nums2[index2]
                elif index2 == len2:
                    right_min = nums1[index1]
                else:
                    right_min = min(nums1[index1], nums2[index2])
                return (left_max + right_min) / 2
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        end1 = len(nums1)
        end2 = len(nums2)
        k1 = (end1 + end2 + 1) // 2
        k2 = (end1 + end2) // 2 + 1
        if end1 <= end2:
            return (self.find_kth_smallest(k1, nums1, nums2, 0, end1, 0, end2) + self.find_kth_smallest(k2, nums1, nums2, 0, end1, 0, end2)) / 2
        else:
            return (self.find_kth_smallest(k1, nums2, nums1, 0, end2, 0, end1) + self.find_kth_smallest(k2, nums2, nums1, 0, end2, 0, end1)) / 2

    # end2 - begin2 >= end1 - begin1 to make sure it works
    def find_kth_smallest(self, k, nums1, nums2, begin1, end1, begin2, end2):
        # print(k, nums1, nums2, begin1, end1, begin2, end2)
        if k <= 0 or k > end1 + end2 - begin1 - begin2:
            return None
        if begin1 >= end1:
            return nums2[begin2 + k - 1]
        if begin2 >= end2:
            return nums1[begin1 + k - 1]
        if k == 1:
            return min(nums1[begin1], nums2[begin2])
        range1 = k // 2
        if begin1 + range1 - 1 >= end1:
            range1 = end1 - begin1
        range2 = k - range1
        index1 = begin1 + range1 - 1
        index2 = begin2 + range2 - 1
        if nums1[index1] >= nums2[index2]:
            if index2 + 1 == end2:
                return nums1[index1]
            else:
                if nums2[index2 + 1] >= nums1[index1]:
                    return nums1[index1]
                else:
                    end1 = index1
                    begin2 = index2 + 1
                    if end2 - begin2 >= end1 - begin1:
                        return self.find_kth_smallest(range1, nums1, nums2, begin1, end1, begin2, end2)
                    else:
                        return self.find_kth_smallest(range1, nums2, nums1, begin2, end2, begin1, end1)
        else:
            if index1 + 1 == end1:
                return nums2[index2]
            else:
                if nums1[index1 + 1] >= nums2[index2]:
                    return nums2[index2]
                else:
                    end2 = index2
                    begin1 = index1 + 1
                    if end2 - begin2 >= end1 - begin1:
                        return self.find_kth_smallest(range2, nums1, nums2, begin1, end1, begin2, end2)
                    else:
                        return self.find_kth_smallest(range2, nums2, nums1, begin2, end2, begin1, end1)                    


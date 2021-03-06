"""
problem 23: Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

solution:
    https://leetcode.com/problems/merge-k-sorted-lists/solution/

"""  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def divide(l, r):
            if l <= r:
                middle = l + (r - l) // 2
                left = divide(l, middle)
                right = divide(middle + 1, r)
                return merge(left, right)
            else:
                return None

        def merge(left, right):
            dummy = ListNode(0)
            head = dummy
            while left or right:
                if left is None:
                    head.next = right
                    break
                elif right is None:
                    head.next = left
                    break
                else:
                    if left.val <= right.val:
                        head.next = left
                        left = left.next
                    else:
                        head.next = right
                        right = right.next
                    head = head.next
            return dummy.next

        return divide(0, len(lists) - 1)

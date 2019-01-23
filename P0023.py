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


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        def merge2(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            head = ListNode(0)
            previous = head
            while l1 and l2:
                if l1.val <= l2.val:
                    previous.next = l1
                    previous = l1
                    l1 = l1.next
                else:
                    previous.next = l2
                    previous = l2
                    l2 = l2.next
            if l1:
                previous.next = l1
            if l2:
                previous.next = l2
            return head.next
        def merge(lists, start, end):
            if start >= end:
                return lists[start]
            middle = (start + end) // 2
            return merge2(merge(lists, start, middle), merge(lists, middle+1, end))
        return merge(lists, 0, len(lists)-1)
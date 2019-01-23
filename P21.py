"""
problem 21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

solution:
    https://leetcode.com/problems/valid-parentheses/solution/

"""  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy_node = head
        while l1 or l2:
            if l1 is None:
                dummy_node.next = l2
                break
            if l2 is None:
                dummy_node.next = l1
                break
            else:
                if l1.val <= l2.val:
                    dummy_node.next = l1
                    l1 = l1.next
                else:
                    dummy_node.next = l2
                    l2 = l2.next
                dummy_node = dummy_node.next
        return head.next
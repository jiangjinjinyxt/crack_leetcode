"""
problem 160: Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/solution/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        len_a = 0
        len_b = 0
        dummy = headA
        while dummy:
            len_a += 1
            dummy = dummy.next
        dummy = headB
        while dummy:
            len_b += 1
            dummy = dummy.next
        if len_a < len_b:
            len_a, len_b = len_b, len_a
            headA, headB = headB, headA
        for i in range(len_a - len_b):
            headA = headA.next
        for i in range(len_b):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
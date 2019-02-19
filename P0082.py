"""
problem 82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy_node = ListNode(None)
        dummy_node.next = head
        start_node = dummy_node
        
        previous_node = dummy_node.next
        previous_val = previous_node.val
        count = 1

        current_node = previous_node.next

        while current_node:
            if current_node.val == previous_val:
                count += 1
            else:
                if count == 1:
                    start_node = previous_node
                else:
                    start_node.next = current_node
                    count = 1
                previous_node = current_node
                previous_val = current_node.val
            current_node = current_node.next

        if count > 1:
            start_node.next = None
        return dummy_node.next




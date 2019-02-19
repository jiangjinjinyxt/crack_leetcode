"""
problem 83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

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
        dummy_head = ListNode(None)
        dummy_head.next = head
        previous_node = dummy_head
        current_node = dummy_head.next
        while current_node:
            if current_node.val == previous_node.val:
                previous_node.next= current_node.next
            else:
                previous_node = current_node
            current_node = current_node.next
        return dummy_head.next
                    


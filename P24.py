"""
problem 24: Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/


solution:
    

"""  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head

        previous = dummy_node

        while previous.next and previous.next.next:
        	next_node = previous.next
        	previous.next = next_node.next
        	next_node.next = next_node.next.next
        	previous.next.next = next_node
        	previous = next_node
        return dummy_node.next


"""
problem 25: Reverse Nodes in K-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/


solution:
    

"""  


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        flag = True
        while flag:
            temp = previous
            node_list = []
            for i in range(k):
                if temp.next:
                    node_list.append(temp.next)
                    temp = temp.next
                else:
                    flag = False
                    break
            else:
                next_node = temp.next
                node_list[0].next = next_node
                previous.next = node_list[-1]
                for idx in range(k - 1, 0, -1):
                    node_list[idx].next = node_list[idx - 1]
                previous = node_list[0]
        return dummy.next



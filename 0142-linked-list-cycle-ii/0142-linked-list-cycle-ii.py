# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        index=0
        if not head or not head.next:
            return None
        while fast and fast.next:
            slow, fast=slow.next, fast.next.next
            if slow==fast:
                break
        else:
            return None
        
        slow=head
        while slow!=fast:
            slow, fast=slow.next, fast.next
            index+=1
        return slow
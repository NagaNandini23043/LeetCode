# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        if slow==fast:
            head=None
            return head
        else:
            pre.next=slow.next
            slow.next=None
        return head
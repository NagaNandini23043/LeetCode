# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        dummy=ListNode(0)
        curr=dummy
        while slow:
            curr.next=ListNode(slow.val)
            curr=curr.next
            slow=slow.next
        return dummy.next
        
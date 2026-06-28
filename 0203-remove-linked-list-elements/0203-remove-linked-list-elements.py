# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        temp=ListNode(0)
        temp.next=head
        pre=temp
        curr=head

        while curr:
            if curr.val==val:
                pre.next=curr.next
            else:
                pre=curr
            curr=curr.next
            
        return temp.next
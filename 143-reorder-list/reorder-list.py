# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        prev= slow.next =None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        first,sec=head,prev

        while sec:
            temp1,temp2=first.next,sec.next
            first.next=sec
            sec.next=temp1
            first,sec=temp1,temp2

        return first
        
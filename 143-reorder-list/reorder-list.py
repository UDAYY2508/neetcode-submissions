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
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        sec=slow.next
        prev=slow.next=None
        while sec:
            nex=sec.next
            sec.next=prev
            prev=sec
            sec=nex
        fir,sec=head,prev
        while sec:
            temp1,temp2=fir.next,sec.next
            fir.next=sec
            sec.next=temp1
            fir=temp1
            sec=temp2

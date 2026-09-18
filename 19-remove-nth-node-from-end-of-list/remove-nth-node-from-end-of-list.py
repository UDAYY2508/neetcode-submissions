# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
       
        start = ListNode(0,head)
        left = start
        right = head

        while right and n>0:
            right = right.next
            n-=1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next 

        return start.next

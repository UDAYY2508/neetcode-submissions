# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None  
        prev = None
        while sec:
            nextN = sec.next
            sec.next = prev
            prev = sec
            sec = nextN
        
        first,second = head,prev

        while second:
            t1 , t2 = first.next,second.next
            first.next = second
            second.next = t1
            first,second = t1,t2




        
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mp = {}
        curr=head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        
        curr=head
        while curr:
            copy = mp[curr]
            copy.random = mp.get(curr.random)
            copy.next = mp.get(curr.next)
            curr = curr.next

        return mp.get(head)







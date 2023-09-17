'''
Given the head of a singly linked list, group all the nodes with odd indices together followed 
by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain 
as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

'''
solution

1.if head is none return none
2.initialize two pointers even and odd
3.assign head to odd and head.next to even
4.create evenhead and assign even to evenhead
5.here we are linking all the odd nodes and even nodes seperately
6. finally we are linking even nodes at the end of odd nodes
7. run a while loop until even and even.next is not None
8.odd.next becomes odd.next.next
9then iterate odd to odd.next
10. similarly even.next becomes even.next.next
11. iterate even to even.next
12.then link even head to odd.next
13. return the head

'''

#solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        odd=head
        even=evenHead=head.next

        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next
        odd.next=evenHead

        return head
        
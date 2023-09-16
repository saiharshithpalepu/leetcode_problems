'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list 
that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
'''

'''
solution

1.create a dummy head
2.then assign the original head to the next pointer of dummy head
3.assign dummyhead to current
4.run the while loop while the next pointer of current is not None
5.if given value is equal to current.next value then make current is equal to current.next.next
6.otherwise make current to current.next
7.return dummyhead.next
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead=ListNode()
        dummyHead.next=head

        current=dummyHead

        while current.next is not None:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next

        return dummyHead.next
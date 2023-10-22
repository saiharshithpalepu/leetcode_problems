'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

'''
solution
1.consider there are 5 nodes in the linked list. If the k is given 2
2.then we have to attach the last two nodes of the linked list at the head
3. for this we need to traverse till the point before the last two nodes
4.if k is greater than the length of the linked list
5. we have to mod the k with the length and gshould get the modulus.
6.after getting the two nodes
7.we have to make last node of pivot points as none
8.then we have to attach this list to new head
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        current=head
        for i in range(length-k-1):
            current=current.next
        new_head=current.next
        current.next=None
        tail.next=head
        return new_head
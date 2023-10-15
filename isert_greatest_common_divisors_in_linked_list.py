'''Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the 
greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both 
numbers.

 

Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the 
linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:


Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the 
linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
 
'''

'''
solution
1.if the linked list is empty then return it
2.assign head of a linkedlist to a temp variable
3.run the while loop while the temp.next is not None
4.create a new node and assign value of gcd of current node and next node
5.then assign next of temp  to next of new node
6.then assign new node to next of temp
7.then make temp as temp.next.next
8.finally return the linked list
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp=head
        if(not temp):
            return head
        else:
            while temp.next is not None:
                new_node=ListNode(math.gcd(temp.val,temp.next.val))
                new_node.next=temp.next
                temp.next=new_node
                temp=temp.next.next
            return head
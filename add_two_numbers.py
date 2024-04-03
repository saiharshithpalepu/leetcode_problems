'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
#solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead=ListNode(0)
        tail=dummyHead
        carry=0

        while l1 is not None or l2 is not None or carry!=0:
            if l1 is not None:
                digit1=l1.val
            else:
                digit1=0

            if l2 is not None:
                digit2=l2.val
            else:
                digit2=0

            sum1=digit1+digit2+carry

            new_val=sum1%10
            carry=sum1//10
            new_node=ListNode(new_val)
            tail.next=new_node
            tail=tail.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        
        tail.next=None
        result=dummyHead.next
        return result
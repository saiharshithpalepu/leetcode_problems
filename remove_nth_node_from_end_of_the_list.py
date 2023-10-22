'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''

'''
solution
1.first we need to find the length of the list
2.then we will get the before node where we are going to remove the node
3.then we will iterate to that node
4.then we will change the next pointer of the node
5.through this we can remove the node
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count1=0
        temp=head
        while temp:
            count1+=1
            temp=temp.next
        lastIndex=count1-n
        if lastIndex==0:
            return head.next
        else:
            temp1=head
            count2=0
            while temp1 is not None:
                count2+=1
                if count2==lastIndex:
                    new_node=temp1.next
                    temp1.next=temp1.next.next
                    new_node.next=None
                    return head

                else:
                    temp1=temp1.next

        
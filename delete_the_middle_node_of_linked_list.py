'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified
 linked list.The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 
 0-based indexing,where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
'''

'''
1.create two pointers slow and fast and initialize both of them to head
2. if the next pointer of fast is None then return None because it does not have any middle node
3.other wise run the while loop until fast and fast.next is not none
3.move the slow pointer to slow.next
4.move the fast pointer to fast.next.next
5. by the time fast reaches the end slow will be exactly at the middle
6. now we got the middle node
7.the run the loop again
8. if the temp node .next is slow then assign temp.next = temp.next.next
9. i the above step we are breaking the link of the middle node
10. so middle none will not be there in the linked list
11. finally return the head
'''

#solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if fast.next is None:
            return None
        else:
            while fast is not None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next

            temp=head
            while temp is not None:
                if(temp.next==slow):
                    temp.next=temp.next.next
                    
                else:
                    temp=temp.next
            return head
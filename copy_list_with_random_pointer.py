'''
Intuition
The description of the problem is quite complex to understand but the solution is vey simple.

In this problem a linked list is given and it has n nodes. Each node has three properties val, next and random pointer(which might point to any node in the llinkedlist)

for the solution we have to create a linkedlist exactly as the original linkedlist but any of the nodes present in the new linkedlist should not reference to nodes in old linkedlist

Approach
if there is no random pointer we can create the copy of the linkedlist using a single while loop.

but for this problem due to the existence of random pointer we need to use two while loops.

Reason for using two loops:
if we use only one loop we can easily get the next pointer but getting random pointer becomes tricky.you can refer the below example to understand this

eg:
consider if node 0's random pointer is pointed towards node5 In this scenario we would not have created node 5 so we cannot point it using a single while loop.

Approach:

we will create a dictionary which stores values of old nodes as keys and corresponding new nodes as its values.

by running the first loop we will populate the dictionary with the old nodes and the corresponding new nodes(by creating a new node)

in the second while loop we will assign the values of next and random pointers by getting the values from dictionary

Please go through the below code you will understand the solution thoroughly

Complexity
Time complexity:
we are using two while loops so time complexity will be O(n+n)=O(2n)=O(n)

Space complexity:
we are use dictionary it will take O(n) space
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        oldToCopy={None:None}
        cur=head

        while cur:
            copy=Node(cur.val)
            oldToCopy[cur]=copy
            cur=cur.next

        cur=head
        while cur:
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next

        return oldToCopy[head]
        
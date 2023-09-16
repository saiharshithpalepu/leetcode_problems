'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''

#mysolution
'''
1. I have created an empty list
2. then i have iterated through the linked list and appended the node values to the list if they are
not in the list
3.I am returning true if the condition goes to else [it will only go to else if it has cycle]
4,otherwise return False
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head) :

       list1=[]
       temp=head
       while temp is not None:
           if temp not in list1:
               list1.append(temp)
           else:
               return True
           temp=temp.next
       return False
    
#solution 2

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

       dictionary={}
       temp=head
       while temp is not None:
           if temp in dictionary:
               return True
           else:
               dictionary[temp]=True 
           temp=temp.next
       return False
    
#solution 3 using pointers

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
           
        
           

        
        
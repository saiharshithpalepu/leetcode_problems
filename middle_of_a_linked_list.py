'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

'''
solution 
1.we create two pointers .first one is slow and second one is fast
2. we check while fast and fast.next is not None
3.we move slow to slow.next
4.fast to fast.next
5.by the time fast reaches the endpoint slow will be exactly at the middle#
6. we will retuen the slow
'''
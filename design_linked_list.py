'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
'''

#solution
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def get(self, index: int) -> int:
        count1=0
        temp=self.head
        while temp is not None:
            print(temp.val,'temp.val',count1,'count1',index,'index')
            if index==count1:
                return temp.val
            temp=temp.next
            count1+=1
        return -1

        
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        elif index==0:
            new_node=Node(val)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                new_node.next=self.head
                self.head=new_node
        elif index==self.length:
            new_node=Node(val)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
                self.tail=new_node
        else:
            new_node=Node(val)
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            print(temp.val,'insert at index')
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length:
            return
        elif index==0:
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                new_node=self.head
                self.head=self.head.next
                new_node.next=None
        elif index==self.length-1:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=None
            self.tail=temp
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            deleted_node=temp.next
            temp.next=temp.next.next
        self.length-=1





        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
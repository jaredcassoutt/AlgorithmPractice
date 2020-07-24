
class Node:
    '''
    This class designates a node for a linked list with a given data point
    and pointer. The data point and pointer are both None unless specified otherwise.
    '''
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    '''
    This class creates is used to create a linked list. It initially needs a head.
    Once given this head, the list can be traversed, a new head can be given, a new
    tail can be given, a item can be inserted after a specified item, and a
    specified item can be removed from the list.
    '''
    def __init__(self):
        self.head = None
        
    def traverse(self):
        print_val = self.head
        while print_val:
            print(print_val.data)
            print_val = print_val.next
            
    def newHead(self,new_val):
        new_head = Node(new_val)
        new_head.next = self.head
        self.head = new_head
        
    def newTail(self,new_val):
        new_tail = Node(new_val)
        if self.head == None:
            self.head = new_tail
            return
        traversing = self.head
        while traversing.next:
            traversing = traversing.next
        traversing.next = new_tail
        
    def insertAfter(self,node_after,new_val):
        if node_after is None:
            print("No Node Exists")
            return
        new_node = Node(new_val)
        new_node.next = node_after.next
        node_after.next = new_node
        
    def remove(self,node):
        if node is None:
            print("No Node Exists")
            return
        node_before = self.head
        node_at = self.head.next
        while node_at != node:
            node_before = node_at
            node_at = node_at.next
        if node_at.next is not None:
            node_before.next = node_at.next
        else:
            node_before.next = None

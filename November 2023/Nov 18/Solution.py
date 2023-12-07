#Alternate solution to use a stack to reverse the elements
class Solution:
    def reverseDLL(self, head):
        newHead=None
        while(head):
            temp=head.next
            head.next=head.prev
            head.prev=temp
            if head.prev==None:
                newHead=head
            head=head.prev
        return newHead

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
   
    def push(self, new_data,tail):
        if not self.head:
            self.head=Node(new_data)
            return self.head
        Nnode=Node(new_data)
        Nnode.prev=tail
        tail.next=Nnode
        return Nnode
        
    def printList(self, node): 
        while(node is not None): 
            print (node.data,end=' ') 
            node = node.next

if __name__ == '__main__':
    
    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
    dll=DoublyLinkedList()
    tail=None
    
    for e in arr:
        tail=dll.push(e,tail)
    
    ob = Solution()
    resHead=ob.reverseDLL(dll.head)
    dll.printList(resHead)
    print()
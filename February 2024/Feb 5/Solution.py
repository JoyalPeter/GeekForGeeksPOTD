class Solution:
    def sortedInsert(self, head, data):
        newNode=Node(data)
        
        #if list is empty
        if head==None:
            head=newNode
            newNode.next=head
            return head
        
        #if list contains only one element
        if head.next==head:
            head.next=newNode
            newNode.next=head
            if data<head.data:
                head=newNode
                return head
            else:
                return head
        
        #if data is less than the first element
        if data<head.data:
            newNode.next=head
            prev=head
            temp=head.next
            while(temp!=head):
                prev=temp
                temp=temp.next
            prev.next=newNode
            head=newNode
            return head
            
        prev=head
        temp=head.next
        while temp!=head:
            if data<temp.data:
                break
            prev=temp
            temp=temp.next
        
        prev.next=newNode
        newNode.next=temp
        return head

class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    arr=[1,2,4]
    data=3
    cll=LinkedList()
    for e in arr:
        cll.push(e)
        
    reshead=Solution().sortedInsert(cll.head,data)
    printList(reshead)
    print()
    


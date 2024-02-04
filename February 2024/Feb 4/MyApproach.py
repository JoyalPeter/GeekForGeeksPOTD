class Solution:
    def generateNumber(self, head):
        num = 0
        while head:
            num = num * 10 + head.data
            head = head.next
        return num

    def subLinkedList(self, l1, l2):
        num1 = self.generateNumber(l1)
        num2 = self.generateNumber(l2)
        diff = str(num1 - num2) if num1 > num2 else str(num2 - num1)
        newLL = LinkedList()
        for i in diff:
            newLL.insert(int(i))
        return newLL.head

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end="")
        n = n.next
    print()


if __name__ == "__main__":

        arr1 = [1,0,0]
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        arr2 = [1,2]
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)

        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)

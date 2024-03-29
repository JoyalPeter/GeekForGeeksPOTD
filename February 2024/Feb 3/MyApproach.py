class Solution:
    def decimalValue(self, head):
        MOD = 10**9 + 7
        num = 0
        while head:
            num = num * 10 + head.data
            head = head.next

        return int(str(num), 2) % MOD

# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


# Driver Program
if __name__ == "__main__":
        list1 = Linked_List()
        values = [0,1,1]
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.decimalValue(list1.head))

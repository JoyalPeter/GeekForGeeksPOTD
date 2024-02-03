class Solution:
    def decimalValue(self, head):
        MOD = 10**9 + 7
        res = 0
        while head is not None:
            res = ((res * 2) % MOD + head.data) % MOD  #if res*10 then decimal, if res*16 then hex, if res*2 then binary
            head = head.next

        return res


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
    values = [0, 1, 1]
    for i in values:
        list1.insert(i)
    ob = Solution()
    print(ob.decimalValue(list1.head))

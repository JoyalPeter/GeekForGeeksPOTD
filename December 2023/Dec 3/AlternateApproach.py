from collections import deque

"""The idea is to traverse BST 1 from smallest value to node to largest.
Traverse BST 2 from largest value node to smallest. 
The approach uses a stack-based iterative traversal of both BSTs simultaneously.
By comparing the sum of the values of the current nodes in the two BSTs with the target x."""
class Solution:
    # Function to count pairs with a given sum in two BSTs.
    def countPairs(self, root1, root2, x):
        # if either of the trees is empty, return 0.
        if (root1 is None) or (root2 is None):
            return 0

        # using stacks to store the nodes of the trees.
        st1 = []
        st2 = []

        # creating dummy nodes for the top of the stacks.
        top1 = Node(-1)
        top2 = Node(-1)

        # variable to keep track of the count of pairs.
        count = 0

        # iterating through the trees.
        while 1:
            # traversing the left subtree of the first tree and
            # appending the nodes to stack1.
            while root1 != None:
                st1.append(root1)
                root1 = root1.left

            # traversing the right subtree of the second tree and
            # appending the nodes to stack2.
            while root2 != None:
                st2.append(root2)
                root2 = root2.right

            # if either of the stacks are empty, break the loop.
            if (len(st1) == 0) or (len(st2) == 0):
                break

            # getting the top nodes of both stacks.
            top1 = st1[len(st1) - 1]
            top2 = st2[len(st2) - 1]

            # checking if the sum of the top nodes is equal to x.
            if (top1.data + top2.data) == x:
                # if yes, increment the count, remove the top nodes from both stacks,
                # and move to the right child of the top nodes.
                count = count + 1
                st1.pop()
                st2.pop()
                root1 = top1.right
                root2 = top2.left

            # if the sum is less than x, remove the top node from stack1
            # and move to the right child of the top node.
            elif (top1.data + top2.data) < x:
                st1.pop()
                root1 = top1.right

            # if the sum is greater than x, remove the top node from stack2
            # and move to the left child of the top node.
            else:
                st2.pop()
                root2 = top2.left

        # returning the count of pairs.
        return count


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    s1 = "5 3 7 2 4 6 8"
    s2 = "10 6 15 3 8 11 18"
    root1 = buildTree(s1)
    root2 = buildTree(s2)
    x = 16
    ob = Solution()
    print(ob.countPairs(root1, root2, x))

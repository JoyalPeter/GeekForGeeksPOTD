class Solution:

    def iterateTree(self, root, k, height, tree, specialNodes):
        if root == None:
            return
        # height += 1
        if root.left == None and root.right == None:
            if height >= k:
                specialNodes.add(tree)
            return

        tree +=str(root.data)
        self.iterateTree(root.left, k, height + 1, tree, specialNodes)
        self.iterateTree(root.right, k, height + 1, tree, specialNodes)

    # Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        specialNodes = set()
        self.iterateTree(root, k, 0, "", specialNodes)
        print(specialNodes)
        return 0


MAX_HEIGHT = 100000
c = 0
from collections import deque


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
    s = "1 2 3 4 5 6 7 N N N N N 8"
    root = buildTree(s)
    k = 2
    ob = Solution()
    print(ob.printKDistantfromLeaf(root, k))


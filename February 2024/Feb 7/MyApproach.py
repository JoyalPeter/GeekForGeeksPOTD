class Solution:
    def findPath(self, root, element, path):
        if root == None:
            return False
        if root.data == element:
            return path + str(root.data) + "n"
        return self.findPath(
            root.left, element, path + str(root.data) + "n"
        ) or self.findPath(root.right, element, path + str(root.data) + "n")

    def findDist(self, root, a, b):
        pathToA = self.findPath(root, a, "")
        ancestorsA = [int(i) for i in pathToA.split("n") if i != ""]

        pathToB = self.findPath(root, b, "")
        ancestorsB = [int(i) for i in pathToB.split("n") if i != ""]

        shortPath = (
            len(ancestorsA) if len(ancestorsA) < len(ancestorsB) else len(ancestorsB)
        )

        for i in range(0, shortPath):
            if ancestorsA[i] != ancestorsB[i]:
                break
        else:
            i += 1 # a,b share a direct parent child relation

        distance = (len(ancestorsA) - i) + (len(ancestorsB) - i)

        return distance

import sys

sys.setrecursionlimit(50000)
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
        s = "11 22 33 44 55 66 77 N N N N N N N N"
        root = buildTree(s)
        a, b = 22,77
        ob = Solution()
        print(ob.findDist(root, a, b))


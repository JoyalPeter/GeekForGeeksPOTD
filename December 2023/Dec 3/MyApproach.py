from collections import deque

#Find all compliment (X-number) for tree1 and search for them in tree2
class Solution:
    def iterateTree(self, root, arr, x, isTree1):
        if root == None:
            return
        if isTree1:
            arr.add(x - root.data)
        else:
            arr.add(root.data)
        if root.data >= x:
            self.iterateTree(root.left, arr, x, isTree1)
        else:
            self.iterateTree(root.left, arr, x, isTree1)
            self.iterateTree(root.right, arr, x, isTree1)

    def countPairs(self, root1, root2, x):
        tree1 = set()
        self.iterateTree(root1, tree1, x, True)
        tree2 = set()
        self.iterateTree(root2, tree2, x, False)
        pairs = tree1.intersection(tree2)
        return len(pairs)

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
    s1 = '5 3 7 2 4 6 8'
    s2 = '10 6 15 3 8 11 18'
    root1 = buildTree(s1)
    root2 = buildTree(s2)
    x = 16
    ob = Solution()
    print(ob.countPairs(root1, root2, x))

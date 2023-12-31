from collections import deque

# Returns True if trees with roots as root1 and root 2
# are mirror
def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True

    """ For two trees to be mirror images, the following three 
        conditions must be true 
        1 - Their root node's key must be same 
        2 - left subtree of left tree and right subtree 
          of the right tree have to be mirror images 
        3 - right subtree of left tree and left subtree 
           of right tree have to be mirror images 
    """
    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return isMirror(root1.left, root2.right) and isMirror(
                root1.right, root2.left
            )

    # If neither of the above conditions is true then root1
    # and root2 are not mirror images
    return False


class Solution:
    def isSymmetric(self, root):
        # Check if tree is mirror of itself
        return isMirror(root, root)


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
    s = "5 1 1 2 N N 2"
    # s = "1 2 3 N N 4 6 N 5 N N 7 N"
    root = buildTree(s)
    ob = Solution()
    if ob.isSymmetric(root):
        print("True")
    else:
        print("False")

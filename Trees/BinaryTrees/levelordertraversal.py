from collections import deque
class BinaryTree:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def levelordertraversal(root):
    
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left :
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result





node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)

node1.left = node2
node1.right= node3
node2.left = node4
node2.right= node5


result = levelordertraversal(node1)
print(result)

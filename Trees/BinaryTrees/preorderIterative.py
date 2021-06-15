class BinaryTree:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def preOrderTraversal(root):

    stack = []
    stack.append(root)
    result = []
    while stack:
        node = stack.pop()
        
        result.append(node.val)

        if node.right :
            stack.append(node.right)

        if node.left :
            stack.append(node.left)

    
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

result = preOrderTraversal(node1)
print(result)

class BinaryTree:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

def postorderTraversal(root,res):
    
    if root is None:
        return
    
    postorderTraversal(root.left,res)
    postorderTraversal(root.right,res)
    res.append(root.val)


node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)

node1.left = node2
node1.right= node3
node2.left = node4
node2.right= node5

res = []
postorderTraversal(node1,res)
print(res)


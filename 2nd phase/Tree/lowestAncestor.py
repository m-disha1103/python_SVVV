# 1 july 2026
#  find the lowest common ancestor of two nodes
class Node:
    data = 0
    left = None
    right = None
    def __init__(self, val):
        self.data = val
class Tree:
    
    def LCA(self, root, n1, n2):
        if root == None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.LCA(root.left, n1, n2)
        right = self.LCA(root.right, n1, n2)
        if left != None and right != None:
            return root
        if left != None:
            return left
        return right 
mango = Tree()
tree = Node(50)
tree.left = Node(40)
tree.right = Node(60)
tree.left.left = Node(20)
tree.left.right = Node(45)
tree.right.left = Node(55)
tree.right.right = Node(70)

ans = mango.LCA(tree, 40, 50)

if ans != None:
    print("LCA =", ans.data)
else:
    print("Node not found")

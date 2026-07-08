class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:

    def BuildTree(self,lst):
        root=Node(lst[0])
        que=[]
        que.append(root)
        j=1
        while len(que)!=0 and j<len(lst):
            curr =que[0]
            del que[0]   #curr.data<=key True curr.data>=key False
            if lst[j]!=None:
                curr.left=Node(lst[j])
                que.append(curr.left)
            if lst[j+1]!=None:
                curr.right=Node(lst[j+1])
                que.append(curr.right)
            j+=2 
        return root
    
               
    def insert(self, root, val):
        if root==None:
            return Node(val)
        if val < root.data:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def inorder(self, root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


    def preorder(self, root):
        if root==None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    
    def postorder(self, root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def levelOrder(self,root):
        if root==None:
            return
        que=[]
        que.append(root) 
        while len(que)!=0:
            curr = que[0]  
            print(curr.data, end =" ") 
            del que[0]
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)      

# if __name__ == "__main__":
#     bst = BST()
#     root = None
#     values = [50, 30, 70, 20, 40, 60, 80]
#     for i in values:
#         root = bst.insert(root, i)

#     print("Inorder:")
#     bst.inorder(root)
#     print("\nPreorder:")
#     bst.preorder(root)
#     print("\nPostorder:")
#     bst.postorder(root)
#     print("\nLevel Order:")
#     bst.levelOrder(root)

    def rightNode(self,node):
        if node==None:
            return
        root=node
        while root.right!=None:
            root=root.right
        return root
    
    def delete(self, root, key):
        temp=self.rightNode(root.left)
        que=[]
        que.append(root)
        while len(que)!=0:
            curr=que[0]
            del que[0]
            if curr.data==key:
                keyNode=curr
                break
            if curr.left!=None:
                que.append(curr.left)
            if curr.right!=None:
                que.append(curr.right)
        if keyNode!=None:
            keyNode.data=temp.data
            self.dltleaf(root,temp)    

    def dltleaf(self,root,temp):
        que=[]
        que.append(root)
        while len(que)!=0:
            curr=que[0]
            del que[0]
            if curr.left==temp:
                curr.left=None
                return
            else:
                if curr.left!=None:
                    que.append(curr.left)      
            if curr.right==temp:
                curr.right=None
                return
            else:
                if curr.right!=None:
                    que.append(curr.right)              
        return root
    
oak=BST()
root = oak.BuildTree([50,40,60,20,45,55,70])
oak.levelOrder(root)
root=oak.dlt(root,50)
print()

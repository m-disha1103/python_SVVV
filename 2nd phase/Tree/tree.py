# 30 june 2026
# concept of tree
class Node:
    data=0
    left=None
    right=None

    def __init__(self,val):
        self.data=val

class Tree:

    def BuildTree(self,lst):
        root=Node(lst[0])
        que=[]
        que.append(root)
        while (len(que)!=0):
            curr=que[0]
            del que[0]
            if lst[i]!=None:
                newnode=Node(lst[i])
                curr.left=newnode
                que.append(newnode)
            if lst[i+1]!=None:
                newnode=Node(lst[i+1])
                curr.right=newnode
                que.append(newnode)
            i=i+2
        return root        
    
    def dlt(self, root, key):
        if root == None:
            return None

        que = []
        que.append(root)

        keyNode = None
        temp = None

        while len(que) != 0:
            curr = que[0]
            del que[0]

            temp = curr

            if curr.data == key:
                keyNode = curr

            if curr.left != None:
                que.append(curr.left)

            if curr.right != None:
                que.append(curr.right)

        if keyNode != None:
            keyNode.data = temp.data
            self.delLastNode(root, temp)

        return root
    
    def delLastNode(self,root,temp):
        que=[]
        que.append(root)
        while len(que)!=0:
            curr=que[0]
            del que[0]
            if curr==temp:
                curr=None
                return
            if curr.right==temp:
                    curr.right=None
            else:
                if curr.right!=None:
                    que.append(curr.right)
            if curr.left==temp:
                curr.left=None
            else:
                if curr.left!=None:
                    que.append(curr.left)
        return root        


    def preOrder(self,root):  #(Root → Left → Right)
        if root==None:
            return
        print(root.data,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self,root):  #(Left → Root → Right)
        if root==None:
            return 
        self.inOrder(root.left)
        print(root.data ,end=" ")
        self.inOrder(root.right)

    def postOrder(self,root):   #(Left → Right → Root)
        if root==None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)    
        print (root.data, end=" ")

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

    def height(self,root):
        if root==None:
            return 0
        left=self.height(root.left)              
        right=self.height(root.right) 
        return 1+max(left,right)        
    
    m=0
    def diameter(self,root):
        if root==None:
            return 0
        left=self.diameter(root.left)
        right=self.diameter(root.right)
        # left=self.height(root.left) 
        # right=self.height(root.right)
        # return 1+left+right
        self.m=max(self.m,left+right)  
        return 1+max(left,right)
    
    c=0
    def countnodes(self,root):
        if root==None:
            return 0
        self.c+=1
        self.countnodes(root.left)
        self.countnodes(root.right) 

    def isEqual(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.data!=root2.data:
            return False    
        return root1.data==root2.data and self.isEqual(root1.left,root2.left) and self.isEqual(root1.right,root2.right)

if __name__=="__main__":
    # mango=Tree()
    # tree=Node(10)
    # tree.left=Node(20)
    # tree.left.left=Node(40)
    # tree.left.right=Node(50)

    # tree.right=Node(30) 
    # tree.right=Node(30) 

    mango=Tree()
    # tree= mango.BuildTree([10,20,30,40,None,60,70])
    tree2=Node(10)
    tree2.left=Node(20)
    tree2.left.left=Node(40)
    tree2.left.right=Node(50)
    tree2.right=Node(30) 
    tree2.right.left=Node(60)
    tree2.right.right=Node(70) 

    # mango.postOrder(tree)
    # mango.inOrder(tree)
    # mango.preOrder(tree)
    # mango.levelOrder(tree)
    # print(mango.height(tree))
    # print(mango.diameter(tree))
    # # mango.diameter(tree)
    # mango.countnodes(tree)
    # print(mango.c)
    mango.levelOrder(tree2)
    print()
    mango.dlt(tree2,20)
    mango.levelOrder(tree2)
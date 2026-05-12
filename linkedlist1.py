#5 may 2026
#linked list concept
class Node:
    data=0
    next=None
    
    def __init__(self,d,n):
        self.data=d
#         self.next=n

# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)

class solution:
    def createnode(self,d):
        newnode=Node(d)
        return newnode
# 5 May 2026
# Linked List Concept

class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n
class Solution:

    def createnode(self, d):
        newnode = Node(d)
        return newnode

    def addathead(self, head, d):
        newnode = self.createnode(d)
        if head is None:
            head = newnode
            return head
        newnode.next = head
        head = newnode
        return head

    def addattail(self, head, d):
        newnode = self.createnode(d)
        if head is None:
            head = newnode
            return head
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        return head

    def addatindex(self, head, d, index):
        newnode = self.createnode(d)
        if head is None:
            head = newnode
            return head
        if index == 0:
            newnode.next = head
            head = newnode
            return head
        temp = head

        for i in range(index - 1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        return head

    def printlist(self, head):
        if head is None:
            print("List is empty")
            return
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# if __name__ == "__main__":

#     head = None
#     s = Solution()
#     head = s.createnode(10)
#     head = s.addathead(head, 5)
#     head = s.addattail(head, 15)
#     head = s.addattail(head, 20)
#     head = s.addatindex(head, 12, 2)
#     s.printlist(head)

# #output:
# # 5 -> 10 -> 12 -> 15 -> 20 -> None

    def deleteathead(self, head):
        if head is None:
            print("List is empty")
            return head
        head = head.next
        return head
    
    def deletetail(self, head):
        if head == None:
            return 
        if head.next == None:

            return None
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return head
    
    def deletewithdata(self,head,key):
        if head==None or (head.data==key and head.next==None):
            return None
        if head.next==None:
            return head
        if head.data==key:
            head=head.next
            return head
        prev=None
        curr=head
        while curr!=None:
            if curr.data==key:
                prev.next=curr.next
                return head
            prev=curr
            curr=curr.next
        print("Data not found")
        return head

    def deleteatindex(self, head, index):
        if head is None:
            print("List is empty")
            return head

        if index == 0:
            head = head.next
            return head

        temp = head
        for i in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
    
    def findmiddlenode(self, head):
        if head is None:
            print("List is empty")
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast.next==None:
            print(slow.data)
        else:
            print(slow.data)
        return slow.data
    
if __name__ == "__main__":

    head = None
    s = Solution()
    head = s.createnode(10)
    head = s.addathead(head, 5)
    head = s.addattail(head, 15)
    head = s.addattail(head, 20)
    head = s.addatindex(head, 12, 2)
    #output:
    # 5 -> 10 -> 12 -> 15 -> 20 -> None
    head = s.deleteathead(head)
    head = s.deletetail(head)
    head = s.deletewithdata(head, 12)
    head = s.deleteatindex(head, 0)
    #output:
    # 15 -> None
    s.printlist(head)

    #reverse a linked list
    def reverselist(self, head):
        if head is None:
            print("List is empty")
            return None
        prev = None
        curr = head
        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        head = prev
        return head
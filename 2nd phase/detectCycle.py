class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data

class Solution:
    @staticmethod
    def detectCycle(head):
        slow = fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
    
    @staticmethod
    def startOfCycle(head):
        slow = fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                slow = head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1

    @staticmethod
    def printList(head):
        if head == None:
            print("List is empty")
            return
        temp = head
        while temp != None:
            print(temp.data, '->', end=" ")
            temp = temp.next

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = head.next.next

    print(Solution.detectCycle(head))
    print(Solution.startOfCycle(head))
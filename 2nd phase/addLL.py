class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data

class Solution:
    @staticmethod
    def addAtHead(head, data):
        new = Node(data)
        if head == None:
            head = new
        else:
            new.next = head
            head = new
        return head
    
    @staticmethod
    def reverseList(head):
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    @staticmethod
    def addList(head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        
        ans = Node(-1)
        temp1 = Solution.reverseList(head1)
        temp2 = Solution.reverseList(head2)
        c = 0
        while(temp1!=None and temp2!=None):
            sum = temp1.data + temp2.data + c
            ans = Solution.addAtHead(ans, sum%10)
            c = sum//10
            temp1 = temp1.next
            temp2 = temp2.next

        while(temp1!=None):
            sum = temp1.data + c
            ans = Solution.addAtHead(ans, sum%10)
            temp1 = temp1.next
            c = sum//10

        while(temp2!=None):
            sum = temp2.data + c
            ans = Solution.addAtHead(ans, sum%10)
            temp2 = temp2.next
            c = sum//10

        while(c!=0):
            ans = Solution.addAtHead(ans, c%10)
            c = c//10

        return ans

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
    head1 = Node(7)
    head1.next = Node(8)
    head1.next.next = Node(6)
    head1.next.next.next = Node(5)
    
    head2 = Node(5)
    head2.next = Node(7)
    head2.next.next = Node(9)
    head2.next.next.next = Node(8)

    Solution.printList(head1)
    print()
    Solution.printList(head2)
    print()
    head3 = Solution.addList(head1, head2)
    # Solution.printList(head3)
    # print()
    temp3 = head3
    while(temp3.next != None):
        print(temp3.data, '->', end=" ")
        temp3 = temp3.next
class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data

class Stack:
    top=None
    size=0
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, top, data):
        new = Node(data)
        if self.top==None:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1
        return self.top
    
    def pop(self, top):
        if self.top==None:
            print("Stack is underflow")
            return self.top
        temp = top
        self.top = self.top.next
        return temp
    
    def peek(self, top):
        if self.top==None:
            return -1
        return self.top.data
    
    def reverse(self, top):
        prev = None
        curr = self.top
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.top = prev
        # return prev
    
    def contains(self, top, key):
        if self.top==None:
            return False
        temp = self.top
        while temp!= None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def merge(self, top1, top2):
        if top1==None:
            return top2
        if top2==None:
            return top1
        
        rev = top2.reverse(top2)
        ans = rev
        while ans!=None:
            node = ans.pop(ans)
            top1.push(top1, node.data)
            ans = ans.next

        return top1
    
    def middle(self, top):
        slow = fast = self.top
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        if fast.next == None:
            return slow.data
        else:
            return slow.data, slow.next.data
    
    def display(self, top):
        if self.top==None:
            print("Stack is underflow")
            return self.top
        temp = self.top
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    s = Stack()
    s.push(s.top, 10)
    s.push(s.top, 20)
    s.push(s.top, 30)
    s.push(s.top, 40)
    s.push(s.top, 50)

    s.display(s.top)
    print()

    s.pop(s.top)

    s.display(s.top)
    print()

    print(s.peek(s.top))

    s.reverse(s.top)
    s.display(s.top)
    print()

    print(s.contains(s.top, 30))
    print(s.contains(s.top, 70))

    print(s.middle(s.top))

    s2 = Stack()
    s2.push(s2.top, 12)
    s2.push(s2.top, 24)
    s2.push(s2.top, 36)

    s1 = Stack()
    s1 = s1.merge(s.top, s2.top)
    s1.display(s1.top)
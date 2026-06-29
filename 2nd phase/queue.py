#24 june 2026
# Queue implementation using list
class Node:
    data=0
    next=None
    def __init__(self,data):
        self.data=val
class Queue:
    size=0
    front,rear=None,None

    def enqueue(self,val):
        newnode=Node(val)
        if self.rear==None:
            self.rear=newnode
            self.front=newnode
            self.size+=1
            return
        self.rear.next=newnode    
        self.rear=newnode
        self.size+=1

    def dequeue(self):
        if self.front==None:
            return -1
        val=self.front.data
        self.front=self.front.next
        self.size-=1
        return val
    
    def peek(self):
        if self.front==None:
            return -1
        return self.front.data
    
    def contains(self, key):
        if self.front == None:
            return False
        temp = self.front
        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def reverse(self):
        self.rear = self.front
        prev = None
        current = self.front
        while current!=None:
            agla= current.next
            current.next = prev
            prev = current
            current = agla
        self.front = prev
        
    def display(self):
        if self.front==None:
            print("Queue is empty")
            return
        temp=self.front
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next    

if __name__=="__main__":
    q=Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.display()
    print()
    q.dequeue()
    q.display()
    print()
    print(q.peek())
    print()
    q.enqueue(30)
    q.display()
    
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

# Stack using 2 queue 
class stack :

    def push(self, que, ele):
        que.enqueue(ele)

    def pop(self,que):
        temp=que.front
        while temp.next.next!=None:
            temp=temp.next
            value=temp.next.data
        temp.next=None
        que.rear=temp            

        return val
    
    def display(self, que):
        if que.front == None:
            return
        temp = que.front
        s=''
        while temp != None:
            s=str(temp.data)+" "
            temp = temp.next
        print(s)



if __name__ == "__main__":
    q = Stack()
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    q.push(50)
    q.push(60)

    st.display()
    print()
    q.dequeue()
    q.display()
    print()
    print(q.peek())
    print()
    q.enqueue(30)
    q.display()
    
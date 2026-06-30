class CircularQueue:
    def __init__(self, n):
        self.size = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        # Queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data

    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            print("Queue Underflow")
            return

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# Driver Code
q = CircularQueue(3)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.dequeue()

q.enqueue(4)

q.display()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            print("Queue Overflow")
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue Underflow")
            return None
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def is_empty(self):
        return self.count == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue contents (front to rear):", end=" ")
        temp_queue = Queue(self.size)
        while not self.is_empty():
            value = self.dequeue()
            print(value, end=" ")
            temp_queue.enqueue(value)
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
        print()

    def search(self, value):
        if self.is_empty():
            return False
        temp_queue = Queue(self.size)
        found = False
        while not self.is_empty():
            front = self.dequeue()
            temp_queue.enqueue(front)
            if front == value:
                found = True
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())
        return found


queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  
print("Dequeued element:", queue.dequeue()) 
queue.display()  
print("Is queue empty?", queue.is_empty())  
print("Is the element 20 belong to queue ",queue.search(20))




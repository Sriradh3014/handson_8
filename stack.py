class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack contents (top to bottom):", end=" ")
        temp_stack = Stack(self.size)
        while not self.is_empty():
            temp_stack.push(self.peek())
            print(self.pop(), end=" ")
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        print()

    def search(self, value):
        if self.is_empty():
            return False
        temp_stack = Stack(self.size)
        found = False
        while not self.is_empty():
            temp_stack.push(self.peek())
            if self.peek() == value:
                found = True
            self.pop()
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        return found

stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  
print("Top element:", stack.peek())  
print("Popped element:", stack.pop())  
stack.display()  
print("Is stack empty?", stack.is_empty())  
print("Is the element 20 belong to stack ",stack.search(20))




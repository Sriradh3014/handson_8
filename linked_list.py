
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_front(self):
        if not self.head:
            print("List is empty")
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def is_empty(self):
        return self.head is None
    
    def display(self):
        if self.is_empty():
            print("Linked list is empty")
            return
        print("Linked list contents:", end=" ")
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def search(self, value):
        if self.is_empty():
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

linked_list = SinglyLinkedList()
linked_list.insert_front(10)
linked_list.insert_front(20)
linked_list.insert_back(30)
linked_list.display()  
print("Removed front node:", linked_list.remove_front())  
linked_list.display()  
print("Is linked list empty?", linked_list.is_empty())  
print("Is the element 20 belong to linked list ",linked_list.search(20))



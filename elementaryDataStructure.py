class Array:
    def __init__(self):
        self.array = []
    
    def insert(self, index, element):
        """ Insert element at specified index """
        self.array.insert(index, element)
    
    def delete(self, index):
        """ Delete element from specified index """
        if 0 <= index < len(self.array):
            del self.array[index]
    
    def access(self, index):
        """ Access element at specified index """
        if 0 <= index < len(self.array):
            return self.array[index]
        return None
    
    def display(self):
        """ Display all elements in the array """
        print(self.array)

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def insert(self, row, col, value):
        """ Insert value at matrix[row][col] """
        if row < len(self.matrix) and col < len(self.matrix[0]):
            self.matrix[row][col] = value
    
    def access(self, row, col):
        """ Access value at matrix[row][col] """
        if row < len(self.matrix) and col < len(self.matrix[0]):
            return self.matrix[row][col]
        return None
    
    def display(self):
        """ Display the entire matrix """
        for row in self.matrix:
            print(row)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        """ Add an element to the stack """
        self.stack.append(element)
    
    def pop(self):
        """ Remove and return the top element of the stack """
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def peek(self):
        """ View the top element of the stack without removing it """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
    
    def display(self):
        """ Display all elements in the stack """
        print(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        """ Add an element to the queue """
        self.queue.append(element)
    
    def dequeue(self):
        """ Remove and return the first element of the queue """
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None
    
    def peek(self):
        """ View the first element of the queue without removing it """
        if len(self.queue) > 0:
            return self.queue[0]
        return None
    
    def display(self):
        """ Display all elements in the queue """
        print(self.queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        """ Insert node at the head of the list """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, data):
        """ Insert node at the tail of the list """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def delete(self, data):
        """ Delete node by value """
        temp = self.head
        if temp is not None and temp.data == data:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    
    def traverse(self):
        """ Traverse the linked list """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, node):
        """ Add a child node to the current node """
        self.children.append(node)
    
    def display(self, level=0):
        """ Display tree structure """
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)

# Main function to demonstrate the operations
def main():
    # Array Test
    print("Array Operations:")
    arr = Array()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.display()
    arr.delete(1)
    arr.display()
    print("Access element at index 1:", arr.access(1))
    
    # Matrix Test
    print("\nMatrix Operations:")
    mat = Matrix(3, 3)
    mat.insert(0, 0, 5)
    mat.insert(1, 1, 10)
    mat.insert(2, 2, 15)
    mat.display()
    print("Access element at [1][1]:", mat.access(1, 1))
    
    # Stack Test
    print("\nStack Operations:")
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    stack.display()
    print("Pop element:", stack.pop())
    stack.display()
    print("Peek top element:", stack.peek())
    
    # Queue Test
    print("\nQueue Operations:")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Dequeue element:", queue.dequeue())
    queue.display()
    print("Peek front element:", queue.peek())
    
    # Singly Linked List Test
    print("\nSingly Linked List Operations:")
    sll = SinglyLinkedList()
    sll.insert_at_head(1)
    sll.insert_at_tail(2)
    sll.insert_at_tail(3)
    sll.traverse()
    sll.delete(2)
    sll.traverse()
    
    # Tree Test
    print("\nTree Operations:")
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode("Child 1.1"))
    child2.add_child(TreeNode("Child 2.1"))
    root.display()

# Calling the main function to run the tests
if __name__ == "__main__":
    main()

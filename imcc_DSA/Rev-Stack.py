class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, data):
        newnode = StackNode(data)
        newnode.next = self.top
        self.top = newnode
        self.size += 1

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next
        self.size -= 1
        return temp.data

    def printstack(self):
            if self.top==None:
                print("Stack underflow")
                return
            print("stack elements:")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
    
    def reverseUsingQueue(self):
        q = Queue()
        while self.top is not None:
            temp = self.top
            self.top = self.top.next
            q.enqueue(temp.data)
            self.size -= 1

        while q.front is not None:
            self.push(q.dequeue())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return temp.data

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverseUsingStk(self):
        sll = StackUsingLL()
        while self.front is not None:
            sll.push(self.dequeue())

        while sll.top is not None:
            self.enqueue(sll.pop())

####### rev Q:
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print("Original:")
myQueue.printQueue()

myQueue.reverseUsingStk()

print("Reversed:")
myQueue.printQueue()

####### rev stk:

myStack = StackUsingLL()
myStack.push(4)
myStack.push(5)
myStack.push(6)

print("\nOriginal Stack (Top to Bottom):")
myStack.printstack()

myStack.reverseUsingQueue()
print("\nReversed Stack (Top to Bottom):")
myStack.printstack()
class node:
    def __init__(self, value, pr):
        self.data = value  # Fixed: store the value
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        # Case 1: Empty queue or new node has strictly higher priority (smaller number)
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            if self.rear is None:
                self.rear = new_node
            return

        # Case 2: Traverse to find the exact insertion point
        temp = self.front
        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        # Update rear if inserted at the very end
        if new_node.next is None:
            self.rear = new_node

    def display(self):
        temp = self.front
        while temp:
            print(f"({temp.data}, pr:{temp.priority})", end=" -> ")
            temp = temp.next
        print("None")

# Test the priority queue
pq = PriorityQueue()
pq.enqueue(node(100, 2))
pq.enqueue(node(500, 6))
pq.enqueue(node(300, 3))
pq.enqueue(node(600, 1))
pq.enqueue(node(700, 1))  # Changed to 700 to verify FIFO order on ties

pq.display()


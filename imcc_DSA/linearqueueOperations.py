class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements (front to rear):", self.items)


def reverse_queue_using_stack(queue):
    stack = []
    while not queue.is_empty():
        stack.append(queue.dequeue())
    while len(stack) > 0:
        queue.enqueue(stack.pop())


def merge_queues(queue1, queue2):
    merged_queue = Queue()
    for item in queue1.items:
        merged_queue.enqueue(item)
    for item in queue2.items:
        merged_queue.enqueue(item)
    return merged_queue


def check_identical_queues(queue1, queue2):
    return queue1.items == queue2.items


# Example Usage for Question 2:
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print("Queue 1:")
q1.display()

print("\nDequeued from Queue 1:", q1.dequeue())
print("Queue 1 after dequeue:")
q1.display()

print("\nReversing Queue 1 using a stack:")
reverse_queue_using_stack(q1)
q1.display()

q2 = Queue()
q2.enqueue(4)
q2.enqueue(5)
print("\nQueue 2:")
q2.display()

merged = merge_queues(q1, q2)
print("\nMerged Queue:")
merged.display()

print("\nAre Queue 1 and Queue 2 identical?", check_identical_queues(q1, q2))

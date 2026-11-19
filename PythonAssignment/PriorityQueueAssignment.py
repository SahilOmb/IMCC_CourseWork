# CPU Process Scheduling Using Priority Queue Implementation using Linked List

class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, pid, name, priority):

        if priority not in [1, 2, 3, 4]:
            print("Invalid Priority! Enter priority between 1 and 4.")
            return

        new_node = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Process added successfully!")

    def dequeue(self):

        if self.front is None:
            print("No processes available!")
            return

        temp = self.front
        print("\nExecuting Process:")
        print("Process ID:", temp.pid)
        print("Process Name:", temp.name)
        print("Priority:", temp.priority)

        self.front = self.front.next

    def display_next(self):

        if self.front is None:
            print("No processes available!")
            return

        print("\nNext Process to Execute:")
        print("Process ID:", self.front.pid)
        print("Process Name:", self.front.name)
        print("Priority:", self.front.priority)

    def display_all(self):

        if self.front is None:
            print("No pending processes!")
            return

        temp = self.front

        print("\nPending Processes:")
        print("ID\tName\t\tPriority")
        print("--------------------------------")

        while temp is not None:
            print(temp.pid, "\t", temp.name, "\t\t", temp.priority)
            temp = temp.next

    def count(self):

        temp = self.front
        total = 0

        while temp is not None:
            total += 1
            temp = temp.next

        print("Total Pending Processes:", total)


pq = PriorityQueue()
while True:
    print("\n===== CPU PROCESS SCHEDULING =====")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Process ID: "))
        name = input("Enter Process Name: ")
        priority = int(input("Enter Priority (1-4): "))

        pq.enqueue(pid, name, priority)

    elif choice == 2:
        pq.dequeue()

    elif choice == 3:
        pq.display_next()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        pq.count()

    elif choice == 6:
        print("Exiting CPU Process Scheduling...")
        break

    else:
        print("Invalid Choice! Please try again.")
        
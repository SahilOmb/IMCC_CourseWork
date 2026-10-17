class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        for value in values:
            self.insert_end(value)

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def findid_del(self):
        while temp1 and temp1.next:
            temp=temp.next
            temp1=temp1.next.next
        print("middlenode:", temp.data)
        prev.next=temp.next
        temp=none


    def insert(self, data, position):
        new_node = Node(data)

        if position <= 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 1):
            if not temp.next:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def middle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data)
        else:
            print("List is empty")

    def delete(self, data):
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

        print()


ll = LinkedList()

values = list(map(int, input("Enter list values: ").split()))
ll.create(values)

print("Linked List:")
ll.display()

data = int(input("Enter value to insert: "))
position = int(input("Enter position: "))
ll.insert(data, position)
ll.display()

print("Middle node:")
ll.middle()

data = int(input("Enter value to delete: "))
ll.delete(data)
ll.display()

print("Reversed list:")
ll.reverse()
ll.display()

print("Sum of consecutive nodes:")
ll.pair_sum()
 
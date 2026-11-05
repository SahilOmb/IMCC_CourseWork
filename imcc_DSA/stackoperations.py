class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements (top to bottom):", self.items[::-1])

def reverse_string_using_stack(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


def reverse_stack_using_another_stack(original_stack):
    temp_stack1 = Stack()
    temp_stack2 = Stack()

    while not original_stack.is_empty():
        temp_stack1.push(original_stack.pop())

    while not temp_stack1.is_empty():
        temp_stack2.push(temp_stack1.pop())

    while not temp_stack2.is_empty():
        original_stack.push(temp_stack2.pop())

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Original Stack:")
my_stack.display()

print("\nPopped element:", my_stack.pop())
print("Stack after pop:")
my_stack.display()

print("\nReversing string 'hello':", reverse_string_using_stack("hello"))

print("\nReversing the stack using another stack:")
reverse_stack_using_another_stack(my_stack)
my_stack.display()

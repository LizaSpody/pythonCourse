# Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_sequence(sequence):
    stack = Stack()

    for char in sequence:
        stack.push(char)

    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence


input_sequence = input("Enter a text:")
reversed_sequence = reverse_sequence(input_sequence)
print("Reversed sequence:", reversed_sequence)
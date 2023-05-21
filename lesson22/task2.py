# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

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



def balanced(text):
    arr = Stack()

    for i in text:
        if i == '(' or i == '{':
            arr.push(i)
        elif i == ')' or i == '}':
            if arr.is_empty():
                return False
            last = arr.pop()
            if (i == ')' and last != '(') or (i == '}' and last != '{'):
                return False

    return arr.is_empty()

line = input('Enter the line:')

print(balanced(line))
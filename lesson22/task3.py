# Extend the Stack to include a method called get_from_stack that
# searches and returns an element e from a stack. Any other element must
# remain on the stack respecting their order. Consider the case in which
# the element is not found - raise ValueError with proper info Message


# Extend the Queue to include a method called get_from_stack that searches
# and returns an element e from a queue. Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

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

    def get_from_stack(self, element):
        found = False
        temp_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            if item == element:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack.")

arr = Stack()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)

try:
    element = arr.get_from_stack(2)
    print("Element found in stack:", element)
except ValueError as e:
    print(e)

try:
    element = arr.get_from_stack(5)
    print("Element found in stack:", element)
except ValueError as e:
    print(e)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        found = False
        temp_queue = Queue()

        while not self.is_empty():
            item = self.dequeue()
            if item == element:
                found = True
                break
            temp_queue.enqueue(item)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the queue.")


arr1 = Queue()
arr1.enqueue(1)
arr1.enqueue(2)
arr1.enqueue(3)
arr1.enqueue(4)

try:
    element = arr1.get_from_queue(2)
    print("Element found in queue:", element)
except ValueError as e:
    print(e)

try:
    element = arr1.get_from_queue(5)
    print("Element found in queue:", element)
except ValueError as e:
    print(e)
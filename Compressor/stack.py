class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        stack_string = ''
        for value in self.items:
            stack_string += str(value)
        return stack_string

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_value(self):
        return str(self)

    def get_items(self):
        return self.items

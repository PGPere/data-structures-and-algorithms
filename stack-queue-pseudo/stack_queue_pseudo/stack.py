class Stack:
    """
    Stack Class
    """

    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

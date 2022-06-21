from stack_queue_pseudo.stack import Stack
from stack_queue_pseudo.node import Node


class PseudoQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):

        while self.s1 is not None:
            self.s2.push(value)
            self.s1.pop()

        self.s1.push(value)

        while self.s2 is not None:
            self.s1.push(value)
            self.s2.pop()

    def dequeue(self):

        if self.s1 is None:
            return "Empty"

        top_value = self.s1.value
        self.s1.pop()
        return top_value

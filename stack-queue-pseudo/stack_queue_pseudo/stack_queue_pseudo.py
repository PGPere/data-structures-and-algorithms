from stack_queue_pseudo.stack import Stack
from stack_queue_pseudo.node import Node


class PseudoQueue():

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if not self.s1.is_empty():
            while self.s1.size() > 0:
                self.s2.push(self.s1.pop())
            pop_item = self.s2.pop()
            while self.s2.size() > 0:
                self.s1.push(self.s2.pop())
            return pop_item

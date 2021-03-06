from stack_and_queue.node import Node
from stack_and_queue.invalid_operation_error import InvalidOperationError
from stack_and_queue.linked_list import LinkedList


class Stack:
    """
    Stack Class
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        # INPUT <-- value to add, wrapped in Node internally
        # OUTPUT <-- none
        # Top = self.top
        node = Node(value)

        if self.top is None:
            self.top = node

        node.next_node = self.top
        self.top = node

    def pop(self):
        # INPUT <-- No input
        # OUTPUT <-- value of top Node in stack
        # EXCEPTION if stack is empty

        if self.top is None:
            raise InvalidOperationError

        node_temp = self.top

        if self.top.next_node is None:
            self.top = None
        elif self.top.next_node is not None:
            self.top = self.top.next_node

        return node_temp.value

    def peek(self):

        if self.top is None:
            raise InvalidOperationError

        return self.top.value

    def is_empty(self):

        if self.top:
            return True

        return False

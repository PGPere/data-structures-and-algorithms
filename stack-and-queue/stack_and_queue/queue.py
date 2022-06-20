from stack_and_queue.node import Node
from stack_and_queue.invalid_operation_error import InvalidOperationError
from stack_and_queue.linked_list import LinkedList


class Queue:
    """
    The quque class
    """

    def __init__(self, rear=None, front=None):
        self.rear = rear
        self.front = front

    def enqueue(self, value):
        # enqueue
        # Arguments: value
        # adds a new node with that value to the back of the queue with an O(1) Time performance.

        node = Node(value)

        front = self.front
        rear = self.rear

        if front is None:
            self.front = node
            self.rear = node
            return

        rear.next_node = node
        self.rear = node

    def dequeue(self):

        if self.front is None:
            raise InvalidOperationError

        front = self.front

        node_temp = self.front

        self.front = self.front.next_node

        node_temp.next_node = None

        return node_temp.value

    def peek(self):

        if self.front is None:
            raise InvalidOperationError

        return self.front.value

    def is_empty(self):

        if not self.front:
            return True

        return False

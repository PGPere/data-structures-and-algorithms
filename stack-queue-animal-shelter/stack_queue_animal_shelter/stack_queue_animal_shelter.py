from stack_queue_animal_shelter.node import Node
from stack_queue_animal_shelter.invalid_operation_error import InvalidOperationError


class AnimalShelter():

    def __init__(self, rear=None, front=None):
        self.rear = rear
        self.front = front

    def enqueue(self, val):
        # enqueue
        # Arguments: dog or cat
        # adds a new node with that value to the back of the queue with an O(1) Time performance.

        node = Node(val)

        front = self.front
        rear = self.rear

        if front is None:
            self.front = node
            self.rear = node
            return

        rear.next_node = node
        self.rear = node

    def dequeue(self, pref):

        if self.front is None:
            return

        while self.front:

            if self.front.value == pref:

                return self.front.value

            node_temp = self.front

            self.front = node_temp.next_node

        node_temp.next_node = None

    def is_empty(self):

        if not self.front:
            return True

        return False


def Dog():
    return 'dog'


def Cat():
    return'cat'

class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:

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
            return None

        front = self.front

        node_temp = self.front

        self.front = self.front.next_node

        node_temp.next_node = None

        return node_temp.value

    def peek(self):

        if self.front is None:
            return None

        return self.front.value

    def is_empty(self):

        if not self.front:
            return True

        return False

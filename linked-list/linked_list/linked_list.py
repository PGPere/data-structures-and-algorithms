class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next_node = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return "True, value exist"
            current = current.next_node

    def __str__(self):
        to_string = ''
        if self.head is None:
            return 'NULL'
        else:
            to_string = ''
            current = self.head
            while current:
                if current.value == self.head.value:
                    to_string = '{ ' + self.head.value + ' } -> '
                else:
                    to_string = to_string + '{ ' + current.value + ' } -> '
                current = current.next_node

            return to_string + 'NULL'


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

    def to_string(self):
        pass

    # def travel_ll(self):
    #     current = self.head
    #     while current:
    #         print(current.value)
    #         current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    # LL [5] -> None
    ll.insert(6)
    # LL [6] -> [5] -> None
    ll.insert(7)
    # LL [7] -> [6] -> [5] -> None
    # ll = LinkedList()
    # brendon = Node(1)
    # brian = Node(2)
    # jae = Node(3)
    # jj = Node(4)
    # roger = Node(5)
    # brendon.next = brian
    # brian.next = jae
    # jae.next = jj
    # ll.head = brendon
    # ll.travel_ll()

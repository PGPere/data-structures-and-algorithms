class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class TargetError(Exception):

    def __init__(self) -> None:
        self.message = "Error"

    def __str__(self):
        return self.message


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """
        This method insert a new node with the given value.
        """
        node = Node(value)

        if self.head is not None:
            node.next_node = self.head
        self.head = node

    def includes(self, value):
        """
        This method confirms if a value is included in the linked list.
        """
        current = self.head

        if not self.head:
            return False

        while current:
            if current.value == value:
                return True
            current = current.next_node
        return False

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

    def append(self, value):
        """
        This method adds a new node with the given value to the end of the list.
        """

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next_node:
            current = current.next_node

        current.next_node = node

    def insert_before(self, target, new_value):
        """
        This method inserts a new node with the given value before the target.
        """

        # tt = TargetError()

        if self.includes(target) == False:
            raise TargetError

        if not self.head:
            return

        current = self.head

        if current.value is target:
            node = Node(new_value)
            node.next_node = self.head
            self.head = node
            return node

        if current.value is not target:
            p = None
            current = self.head
            while current:
                if current.value != target:
                    p = current
                current = current.next_node

            node = Node(new_value)

            node.next_node = p.next_node

            p.next_node = node

        return node

    def insert_after(self, target, new_value):
        """
        This method inserts a new node with the given value after the target.
        """
        if self.includes(target) == False:
            raise TargetError

        if not self.head:
            return

        current = self.head

        if current.value is target:
            node = Node(new_value)
            node.next_node = current.next_node
            current.next_node = node
            return node

        if current.value is not target:
            # p = None
            current = self.head
            while current:
                if current.value != target:
                    # p = current
                    current = current.next_node

            node = Node(new_value)

            node.next_node = current

            current.next_node = node

        return node


# class TargetError(Exception):

#     def __init__(self) -> None:
#         self.message = "Error"

#     def __str__(self):
#         return self.message

    # def insert_after(self, value, new_value):
    #     if self.includes(value) is False:
    #         raise TargetError
    #     current = self.head
    #     while current:
    #         if current.value == value:
    #             node = Node(new_value, current.next_node)
    #             current.next_node = node
    #             break
    #         current = current.next_node

    # def insert_before(self, value, new_value):
    #     if self.includes(value) is False:
    #         raise TargetError
    #     current = self.head
    #     while current:
    #         if current.value == value:
    #             node = Node(new_value, current.next_node)
    #             current.next_node = node
    #             break
    #         current = current.next_node

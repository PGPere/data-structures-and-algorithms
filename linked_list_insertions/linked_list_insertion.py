



class LinkedList:

    def __init__(self, head= None):
    self.head=head

    def append(self, value):
    node = Node(value)
      if self.head is not None:
      node.next = self.head
      self.head = node

    def insert_before(self, value, target):
			pass

		def insert_after(self, value):
  		pass
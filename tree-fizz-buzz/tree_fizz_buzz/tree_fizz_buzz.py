from tree_fizz_buzz.queue import Queue
import copy


def fizz_buzz_tree(tree):

    new_tree = copy.deepcopy(tree)

    queue = Queue()

    collection = []

    queue.enqueue(new_tree.root)

    while not queue.is_empty():

        node = queue.dequeue()

        value = node.value

        if value % 3 == 0 and value % 5 == 0:
            node.value = 'FizzBuzz'
        if value % 3 == 0 and value % 5 != 0:
            node.value = 'Fizz'
        if value % 5 == 0 and value % 3 != 0:
            node.value = 'Buzz'
        else:
            node.value = str(node.value)

        print(node.value)

        collection.append(node.value)
        for child in node.children:
            queue.enqueue(child)

    return new_tree

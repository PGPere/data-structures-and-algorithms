from tree_fizz_buzz.queue import Queue


def fizz_buzz_tree(tree):
    queue = Queue()

    collection = []

    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()

        if node.value % 3 == 0 and value % 5 == 0:
            node.value = 'fizzbuzz'
        if node.value % 3 == 0 and node.value % 5 != 0:
            node.value = 'fizz'
        if node.value % 5 == 0 and node.value % 3 != 0:
            node.value = 'buzz'

        collection.append(node.value)
        for child in node.children:
            queue.enqueue(child)

    return collection

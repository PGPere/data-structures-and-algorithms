from stack_queue_brackets.queue import Queue


def multi_bracket_validation(string):
    open_brackets = ('{([')
    close_brackets = ('})]')
    map = dict(zip(open_brackets, close_brackets))
    queue = Queue()

    for i in string:

        if i in open_brackets:
            queue.enqueue(map[i])
        elif i in close_brackets:
            if i == queue.dequeue():
                return True

    for i in string:
        if i not in open_brackets:
            return False

    if queue.is_empty:
        return True
    else:
        return False

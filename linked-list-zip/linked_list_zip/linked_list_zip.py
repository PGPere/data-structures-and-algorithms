def zip_lists(ll1, ll2):

    if ll1.head is None and ll2.head is None:
        return "Need at least one linked-list"

    elif ll1.head is None:
        return ll2

    elif ll2.head is None:
        return ll1

    current1 = ll1.head
    current2 = ll2.head
    while current1 and current2:
        temp1 = current1.next_node
        temp2 = current2.next_node
        current1.next_node = current2
        if temp1:
            current2.next_node = temp1
        current1 = temp1
        current2 = temp2
        ll2.head = None
    return ll1

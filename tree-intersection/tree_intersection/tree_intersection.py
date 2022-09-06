from tree_intersection.binary_tree import BinaryTree
from tree_intersection.hash_table import Hashtable


def tree_intersection(tree1, tree2):
    list_a_keys = tree1.pre_order()
    list_b_keys = tree2.pre_order()

    hashtable_a = Hashtable()

    hashtable_b = Hashtable()

    for key in list_a_keys:
        hashtable_a.set(str(key), "A")

    for key in list_b_keys:
        hashtable_b.set(str(key), "B")

    inters = []

    for key in list_a_keys:
        if hashtable_b.contains(str(key)):
            inters.append(key)

    return inters

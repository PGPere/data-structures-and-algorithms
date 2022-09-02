from hashtable_left_join.hashtable import Hashtable


def left_join(hashtable1, hashtable2):

    collection = []

    for key in hashtable1.keys():

        words = []
        words.extend([key, hashtable1.get(key), hashtable2.get(key)])
        collection.append(words)

    return collection

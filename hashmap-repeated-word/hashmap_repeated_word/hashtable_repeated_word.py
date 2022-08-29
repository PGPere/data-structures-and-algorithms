
import re
from hash_table.hashtable import Hashtable
from collections import Counter


def first_repeated_word(sentence):

    if sentence == "":
        return None

    sentence = sentence.lower()

    new_sentence = re.sub(r'[^\w\s]', '', sentence)

    print(new_sentence)

    temp = set()

    for word in new_sentence.split():
        if word in temp:
            return word
        else:
            temp.add(word)
    return None

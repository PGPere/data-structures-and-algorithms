
class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):

        index = self.hash(key)

        if self._buckets[index] is not None:

            for kvp in self._buckets[index]:

                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:

                self._buckets[index].append([key, value])
        else:

            self._buckets[index] = []
            self._buckets[index].append([key, value])

    def get(self, key):
        index = self.hash(key)

        if self._buckets[index] is None:
            raise KeyError()
        else:
            for kvp in self._buckets[index]:
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()

    def contains(self, key):
        index = self.hash(key)

        if self._buckets[index] is None:
            raise False
        else:
            for kvp in self._buckets[index]:
                if kvp[0] == key:
                    return True

            return False

    def keys(self):
        keys = []
        indexes = len(self._buckets)
        for n in range(indexes):
            if self._buckets[n] != None:
                keys.append(self._buckets[n][0][0])

        return keys

    def hash(self, key):

        total = 0

        for ch in key:
            total += ord(ch)

        primed = total * 19

        index = primed % self.size
        return index

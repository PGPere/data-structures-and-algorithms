class Merge:

    def __init__(self, arr=[]):
        self.value = arr

    def merge_sort(arr):

        n = len(arr)

        if n > 1:

            # Find the mid
            mid = len(arr)//2

        # Divide the array
            L = arr[:mid]

        # into 2 halves
            R = arr[mid:]

        # Sort the first half
            Merge.merge_sort(L)

        # Sort the second half
            Merge.merge_sort(R)

        # Merge the two halves
            Merge.merge(L, R, arr)
        return arr

    def merge(L, R, arr):

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


if __name__ == "__main__":

    list = [8, 4, 23, 42, 16, 15]

    Merge.merge_sort(list)

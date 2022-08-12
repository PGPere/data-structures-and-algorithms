class Merge:

    def __init__(self, arr=[]):
        self.value = arr

    def merge_sort(arr):

        n = len(arr)

        if n > 1:

            # Finding the mid of the array
            mid = len(arr)//2

        # Dividing the array elements
            L = arr[:mid]

        # into 2 halves
            R = arr[mid:]

        # Sorting the first half
            Merge.merge_sort(L)

        # Sorting the second half
            Merge.merge_sort(R)

            Merge.merge(L, R, arr)

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


class Sort:

    def __init__(self, arr=[]):
        self.value = arr

    def insertion_sort(arr):

        for i in range(1, len(arr)):

            temp = arr[i]
            j = i-1

            while j >= 0 and temp < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp

        return arr


# arr_test = [8, 4, 23, 42, 16, 15]

# insertion_Sort(arr_test)

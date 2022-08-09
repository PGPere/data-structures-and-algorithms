# Insertion Sort

Insertion sort is a sorting algorithm that inserts the unsorted element in the correct order in each iteration.

## Pseudocode

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp


## Trace

Sample : [8,4,23,42,16,15]

### Pass 1

[4, 8, 23, 42, 16, 15]

In the first pass through of the insertion sort, we evaluate if Index 1 contains a smaller number to occupy index 0. We find this is true. Index 1 then becomes Index 0 and Index 0 becomes Index 1.

### Pass 2

[4, 8, 23, 42, 16, 15]

In the second pass through of the insertion sort, we evaluate if index 2 is a smaller number versus index 1. We find current index 1 (i.e. 8) is smaller than Index 2(i.e. 23). Index 1 is 8, no other changes in array.

### Pass 3

[4, 8, 23, 42, 16, 15]

In the third pass through of the insertion sort, we evaluate if index 3 is a smaller number to occupy index 2. We find current index 2 (i.e. 23) is smaller than Index 3(i.e. 42). Index 2 is 23, no other changes in array.

### Pass 4

[4, 8, 16, 23, 42, 15]

In the fourth pass through of the insertion sort, we evaluate if index 4 (i.e. 16) is a smaller number than prior indexes. We find index 4 is smaller than numbers on indexes two and three. Index 4 is moved to index position three.  Indexes two (i.e. 23) and three (i.e. 42) move to indexes three and four respectively.

### Pass 5

[4, 8, 15, 16, 23, 42]

In the fourth pass through of the insertion sort, we evaluate if index 5 (i.e. 15) is a smaller number than prior indexes. We find index 5 is smaller than numbers on indexes two, three and four. Index 5 is moved to index position three.  Indexes two,three,and four move to indexes three, four and five respectively.

## Efficency

Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1)
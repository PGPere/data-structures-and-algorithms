# Merge Sort

This algorythm divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

## Pseudocode

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

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
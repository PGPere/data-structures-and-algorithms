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

[8]

In the first pass through the merge sort, we assign Index 0 to be in the left half.

### Pass 2

[4]

In the second pass through the merge sort, we assign Index 1 to be in the left half.

### Pass 3

[23]

In the third pass through the merge sort, we assign Index 2 to be in the left half.

### Pass 4

[4, 23]

In the fourth pass through the merge sort, we merge an sort the left and right elements of the left side.

### Pass 5

[4, 8, 23]

In the fifth pass through the merge sort, we merge the mid element of the left side.

### Pass 6, 7, 8, 9 ,10

We repeat Pass 1 through Pass 4 for the right side elements

Pass 6 => [42] assign right side

Pass 7 => [16]  assign right side

Pass 8 => [15] assign right side

Pass 9 => [15, 16] merge an sort the two lowest numbers of the right side

Pass 10 => [15, 16, 42] merge an sort the right side

### Pass 11

[4, 8, 15, 16, 23, 42]

We merge both sides.

## Efficency

Time: O(n*Log n)

Space: O(n)

# Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree

## Write a function called fizz buzz tree

## Arguments: k-ary tree

## Return: new k-ary tree

### Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows

#### If the value is divisible by 3, replace the value with “Fizz”

#### If the value is divisible by 5, replace the value with “Buzz”

#### If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

#### If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

![alt text](https://github.com/PGPere/data-structures-and-algorithms/blob/0bb1ee1d2128f7dc8344c9c94ebf4cc9d755a523/tree-fizz-buzz/fizz_buzz_tree.png)

## Approach & Efficiency

### Use breadth first to travserse tree and queue to append into list. Time and space is O(n).
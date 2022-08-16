# Linked List- Find Largest Value

The algorythm will traverse the linked list while head not equal to None.  I decided to initialize Max to 0.  A condition is created to assign if max value is found. Process will end when head is not equal to None. 

## Code

class Node:
 
    def __init__(self):
        self.value = None
        self.next = None
 
head = None
 
def largestValue(head):
 
    max = 0

    if head == None:
        print("No values in Linked List")
        return
 
    while (head != None):
        if (max < head.value) :
            max = head.value
        head = head.next
     
    return max


## Trace

Sample : head -> 12 -> 34 -> 56 -> none

### Pass 1

Initialize max as 0.  Max will help us compare against each node value. 

### Pass 2

Check if there are any values in Linked List.  If no values are found then print ""No values in Linked List". 


### Pass 3

If value is found, then start traversing through linked list.


### Pass 4

Check if head is greater than zero. As 12 is greater than 0, current head of 12 becomes the new max. 


### Pass 5

Traverse then to the the next node.  The next node with value of 34 is now the head.

### Pass 6

Compare the current max of 12 to the new head value of 34.  Now the head with value of 34 becomes the new max.

### Pass 7

Traverse then to the the next node.  The next node with value of 56 is now the head.

### Pass 8

Compare the current max of 34 to the new head value of 56.  Now the head with value of 56 becomes the new max.

### Pass 9

Traverse then to the the next node which is NONE.  

### Pass 10

As Head is NONE then return max value of 56. 


## Efficency

Time: O(n)
The basic operation of this algorithm is comparison. This will happen n number of times…concluding the algorithm.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1)
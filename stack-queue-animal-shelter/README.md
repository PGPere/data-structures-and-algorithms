# Code Challenge 12: First-in, First out Animal Shelter

Create a class called AnimalShelter which holds only dogs and cats.

The shelter operates using a first-in, first-out approach. Implement two methods: enqueue (argument =animal) and dequeue (argument = preference).

## Whiteboard Process

![alt text](https://github.com/PGPere/data-structures-and-algorithms/blob/afc71ad79e8ecf0f3db1b969c910852f99b797a6/stack-queue-animal-shelter/Code%20Challenge%2012.png)

## Approach & Efficiency

My approach is to create an Animal Shelter Class with a enqueue and dequeuue methods.  The dequeue method will go through the queue until it finds the preferred animal between a cat or a dog (only).  The dequeue includes a conditional for identiying requested preference.  If no preference is found in queue, then null is returned.
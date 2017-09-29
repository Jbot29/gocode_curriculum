'''
The bubble sort algorithm compares every two items which are next to each other, 
and swaps them if they are in the wrong order. An array of n elements can be sorted within n-1 passes. 

For example, in this array of 4 items:

First pass:
(4, 3, 1, 2) => (3, 4, 1, 2)
(3, 4, 1, 2) => (3, 1, 4, 2)
(3, 1, 4, 2) => (3, 1, 2, 4)

Second pass:
(3, 1, 2, 4) => (1, 3, 2, 4)
(1, 3, 2, 4) => (1, 2, 3, 4)
(1, 2, 3, 4) => (1, 2, 3, 4)

Third pass:
(1, 2, 3, 4) => (1, 2, 3, 4)
(1, 2, 3, 4) => (1, 2, 3, 4)
(1, 2, 3, 4) => (1, 2, 3, 4)


'''
#write the bubble sort algorithm


def bubble_sort(data):
    pass


assert bubble_sort([6,4,7,8]) == [4,6,7,8]


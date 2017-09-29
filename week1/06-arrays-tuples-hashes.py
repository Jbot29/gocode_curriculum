'''

Arrays/lists are one of the most commonly used data types. They allow us to store multiple instances of some data type. 

In python an array can be heterogeneous, so you can have an array with elements of a mix of data types, even other arrays.


'''

#create an array
result = None

assert result == []

#get the length of an array
a = [1,2]

assert r == 2


#join these two arrays

a = [1,2]
b = [3,4]

assert r == [1,2,3,4]


#get first element out of an array

a = [1,2,3,4]

assert r == 1

#get the last element out of an array

a = [1,2,3,4]

assert r == 4


#reverse an array

a = [1,2,3,4]

assert r == [4,3,2,1]

#sort an array

a = [5,7,24,1]

assert r == [1, 5, 7, 24]

#use the join method to turn the array into a comma separated string - this is tricky because the join method doesn't return the joined object...

a = ["1","2","3"]

assert r == "1,2,3"


#use .append() to append 4 to the array.

r = [1,2,3]

assert r == [1,2,3,4]


#use .pop() to remove an item from an array

a = [1,2,3,4]

assert a ==  [1,2,3] and r == 4


#use .remove() to take an element out of the list

a = [6,7,8,9,6]

assert a == [7, 8, 9, 6]

#use .index() to find the index of 8

a = [6,7,8,9,6]

assert r == 2

#use the in operator to see if 3 is in the array

a = [1,2,3,4]

assert r == True

#use .count() to count the number of instances of an item

a = [6,7,8,9,6]

assert r == 2

#use list() to turn a string into an array of characters

a = "This is a string"

assert r == ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

#turn an array of characters into a string

a = ['c','a','t']

assert r == "cat"


#use the split method to turn the following string into an array
a = "1,2,3"

assert r == ['1', '2', '3']

#slice, get the first three elements of an array
a = ["1","2","3","4","5","6"]

assert r == ["1","2","3"]

#slice get the last three elements of an array
a = ["1","2","3","4","5","6"]

assert r == ["4","5","6"]

#get the middle element

a = ["1","2","3","4","5"]

assert r == "3"


'''

Python and many languages have another data structure called a tuple. It is like an array, except that a tuple is immutable, meaning you can't update it once it is created. 

This can be useful when you want to pass some data around but make sure that no code can update it. Also because they can't be updated, Python can improve performance on them, so they
can be faster then arrays. Outside of updating, you can access tuples in the same way as an array.

Use a tuple when you know the values will not change. This is a good coding practice because it stops any bugs of some accidently screwing up the data. It will also improve the performance of
your code.

'''


#create a tuple

assert r == ()

#get the length of this tuple

a = (1,2)

assert r == 2


#join these two tuples

a = (1,2)
b = (3,4)

assert r == (1, 2, 3, 4)


#get first element out of this tuple

a = (1, 2, 3, 4)

assert r == 1

'''
A dictionary or a hash is a data structure that allows you to associate a key with some other data. This other data can be any other data structure including another dictionary.

'''


#create a hash
r = None

assert r == {}


#add a key 'new_key' to hash with value of 1

r = {}

assert r.has_key('new_key')


#set the value of key 'new_key' to 5

r = {}

assert r['new_key'] == 5


#get all the keys of hash a and set it to r

a = {'a':1,'b':2}

assert r == ['a','b']


#get all the values in this hash and set it to r

a = {'a':1,'b':2}

assert r == [1,2]


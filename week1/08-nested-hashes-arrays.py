'''

Nested data structures are a pain to deal with but very common in programming.

Here are additional exercises to help you get the hang of manipulating these advanced data structures.

You will be doing this quite frequently as a software developer.

'''

#loop through the nested array below and using a nested for loop print all the elements.

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]



#Sum all the numbers in the nested array

a = [[55.00,23.00,46.53],
     [48.98,12.26],
     [99.99,105.04,36.72,33.00]]
     
assert r == 460.52

#Sum all the numbers in the nested hash (both values and keys, if they are numbers)

a = {1:'test','test2':3,3:{4:'test3'}}
     
assert r == 11


# Change r to make the tests pass by creating a nested strcture with the right data inside

r = None

assert type(r) == type({})
assert type(r["Susan"]) == type([])
assert r["Susan"][0] == 93
assert r["Susan"][1] == 78
assert type(r["Jeff"]) == type([])
assert r["Jeff"][0] == 85
assert r["Jeff"][1] == 77


#use r from problem 8 and loop through r to build a new data structure with the
#average grades for Susan and Jeff

avg_grades = None


assert type(avg_grades) == type({})
assert avg_grades["Susan"] == 85.5
assert avg_grades["Jeff"] == 81.0











# Answer these questions - closed book, no notes or Internet.

# Part A. 

# 1) What does an assert statement do?

# 2) Define immutable in the context of data types?  Which data type is immutable and when do you use it?

# 3) What are the common data types used in Python?

# 4) When would you use a for loop and when would you use a while loop?

# 5) What are the 3 major steps outlined in lecture when writing software? 

# Part B. You can use Google and notes.

#1)

r = 42 / 9

assert r == 4.666666666666667

#2)

r = 5 + ".99"

assert r == 5.99

#3)

r = 5 + 9 * 8  

assert r == 112

#4)

r = 4 % 2

assert r == True

#5)

a = 2000.00

r = ""

assert r == "Amount: 2000.00"


#6) create an array of arrays

r = None

assert type(r) == type([])
assert type(r[0]) == type([])

#7) create an array of hashes

r = None

assert type(r) == type([])
assert type(r[0]) == type({})
assert r[0]["key"] == "value"

#8) Sum all the numbers in the nested hash (both values and keys, if they are numbers)

a = {1:'test','test2':{3:'test4'},3:{4:'test3'}}
     
assert r == 11

#9) print all the keys in a
'''
Phone-Number
555-1212
Address
Address2
555-1212
555-1212

'''

a = [{"Phone-Number": {"555-1212":"test"}},{"Address":"555-1213","Address2":{"555-1212":{"555-1212":"test"}}}]

#10) Create a file called 'test.txt' - open it and write "***Blah***" 15 times on 15 different rows.

#11) When should you use an array and when should you use a hash? (We really haven't taught it yet but do some google research and see if you can figure out some reasons.)

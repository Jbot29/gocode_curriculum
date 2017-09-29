'''

Python has a builtin string class to help with common string operations. A string in python is basically a list of characters, with helper methods. Strings do share some commonality with Python lists, which we will cover later.

'''

#create a new string
r = None

assert r == ""

#use len() to find the length of a string
a = "String"

assert r == 6

#put these two string together
a = "Hello "
b = "World"

assert r == "Hello World"


#use * to create five fives
a = "5"

assert r == "55555"

#TODO
#get the first letter of a string
a = "1234"

assert r == "1"

#remove the first character of a string

a = "!Good"

assert r == "Good"

#remove the last character of a string

a = "Good!"

assert r == "Good"

#remove a word from a string

a = "Hello [name]"

assert r == "Hello "

#change "[name]" to "Bob"

a = "Hello [name]"

assert r == "Hello Bob"

#convert the string "5" to 5

a = "5"

assert r == 5

#create a string from a and b
a = "Price = "
b = 5.99

assert r == "Price = 5.99"

#convert the string "5.99" to 5.99

a = "5.99"

assert r == 5.99

#use .format() a string using the string format method

a = '{0}, {1}, {2}'

assert r == 'a, b, c'

#use .rstrip() to remove \n from the string

a = "This is a string with a new line character\n"

assert r == "This is a string with a new line character"

#use .find() to locate the index or where the substring "string" starts in a

a = "Python's string methods are very powerful"

assert r == 9

#use .upper() to uppercase

a = "this is a lower case string"

assert r == 'THIS IS A LOWER CASE STRING'

#use .lower() to lower

a = "THIS IS AN UPPER CASE STRING"

assert r == 'this is an upper case string'

#use .replace() to search and replace "is" with "was"

a = "This is a simple string"

assert r == 'Thwas was a simple string'



# Part A.  Don't look at your notes for this section

#1) Using Big-O notation, describe the worst-case scenario following algorithm:
# What is the best case scenario for the algorithm?

def algo(data):
    swap = True
    while True:   
        for i in range(0,len(data)-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
                swap == True          
        if swap == False:
            return data   
        swap = False


#2) When would you use exceptions in writing a Python program?

#3) Loops Hashes Arrays Re-cap!

'''
print all the keys in d using a for-loop

Output should be
    
Phone-Number
Address
Phone-Number
Address
'''

d = [{"Phone-Number": "555-1212","Address":"306 S. Lamar"},
     {"Phone-Number":"555-1213","Address":"Sonnenallee 14"}]


#4) Solve this iteratively or recursively.  Feel free to use a whiteboard

'''The Fibonacci numbers are the numbers of the following sequence of integer values: 

0,1,1,2,3,5,8,13,21,34,55,89, ... 

The Fibonacci numbers are defined by: 
Fn = Fn-1 + Fn-2 
with F0 = 0 and F1 = 1 

The Fibonacci sequence is named after the mathematician Leonardo of Pisa, who is better known as Fibonacci. In his book "Liber Abaci" (publishes 1202) he introduced the sequence as an exercise dealing with bunnies. His sequence of the Fibonacci numbers begins with F1 = 1, while in modern mathematics the sequence starts with F0 = 0. But this has no effect on the other members of the sequence. 

The Fibonacci numbers are easy to write as a Python function. It's more or less a one to one mapping from the mathematical definition:
'''

#5) Describe the stack data structure.  When would you use it?


# Part B. You can look at your notes for this section


#1) Count the number of instances of each client in the list below, and build a hash with those counts

a = [('client1','blah'),('client1','other'),('client1','other'),('client2','blah'),('client2','other'),('client3','other')]

r = {}

assert r == {'client1': 3, 'client2': 2, 'client3': 1}


#2) Add exception handling around the following

f = open("I-Dont-exist.jpg","r")


#3) Square all the numbers recursively,returning a new list/array

a = [1,2,3,4]

def square_r(values):
    pass

assert square_r(a) == [1,4,9,16]


#4) Update the hash value to be a lambda that adds 2 to a number

a = {"+2":None}

assert a["+2"](5) == 7

#5) Use a list comprehension to add two to all numbers in a

a = [5,7,9]

assert r == [7,9,11]


#6) Write a recursive algorithm that sums all the values of a nested hash

assert sumhash({'a':1,'b':{'c':3}}) == 4
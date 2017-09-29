'''

In an programming language the code can do something so horrible that the computer or interperter doesn't really know how to recover. This is called a crash or an exception.

Divide by zero is an easy way to cause a crash.

That being said, there are many times when we want the program to continue to run. So we need a way to catch these exceptions and recover from them.

This is called exception handling.

Exception handling allows you to wrap some code, and if that code throws an exception, to catch it and continue on.

We start off with a few examples, then a few exercises below.

Please read this following document for an overview of exceptions: 

http://www.tutorialspoint.com/python/python_exceptions.htm

'''

#Examples

try:
    value = 5 / 0
except ZeroDivisionError:
    print "Ooops divide by zero"

    
#Sometimes (many times) you will not really know the exact type of exception being thrown, so you can catch everything

try:
    value = 5 / 0
except:
    print "Can't divide by zero"

#you can also include an else statement to do some work if everything does work out ok
try:
    value = 5 / 1
except:
        print "Can't divide by zero"
else:
    print "Everything worked"


#Finally, there is finally, when you want a block of code to always execute

try:
    value = 5 / 1
finally:
    print "No matter what happens, this line will execute"


#Exercises

#wrap the following code snippets with exception handling


#lets say we ask the user for a number, but they type a bunch of letters instead, the code below would crash
#using a the methods above, wrap this code in a try catch. Bonus if the code tells the user if they did or didn't enter a number

number = raw_input("Please enter a number")
number = number + 10


#if we try to open a file for reading that doesn't exist, or we don't have permission to it will cause a crash
#Wrap the open with exception handling to prevent the crash, and print out that the file does not exist

f = open("idontexist.txt","r")

#go back to your assignments and add exceptions where appropriate - use the above 2 use cases




    

'''

Working with files is a very common task in programming. Many times you will get data in a weird format and have to process it to incorparate it into your application. 

When with working with files you can tell Python and the operating system how you intend to work with the file (read a file or write or append or combinations of these).

'''

#change 'f = None' below.  use open() to with the 'w' argument to create a file called 'blah.txt'

f = None

#note you should always .close() on a file if you use the "w" argument
f.close()

#Here is an example of how to open a file using "r" and closing it afterwards.
f = open("blah.txt", "r")
f.close()

#It can be easy to forget to close a file. Especially in a large amount of code. Forgetting is bad because the operating system may not flush the data to disk (i.e. the system will stall). The operating system tries to optimize disk writing and will sometimes wait until it thinks you are done.

#Python has a better way to interact with files, it is called "with".  Here is an example of how to use the "with" function.

with open("blah.txt", "r") as f:
    print "We now can use f"
    f.read(1)
    print "After this line with will automactically call close on f"

#use with and .write() to write "*Test Data*" to blah.txt


#use .read() to read from blah.txt

assert r == "*Test Data*"


#user .read(1) and a for loop to read and then print all the data in blah.txt



#use with and .readlines() to read from blah.txt

r = None 

assert r == ["*Test Data*"]

#use the "a" flag, write some more data to blah.txt. The "a" says lets append data to this file! Check your file afterwards to make sure it appended what you wrote.


'''
Modes:

Modes Description
r Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

r+ Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

rb+ Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

wb Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


#Extra reading for files including all the modes r/a/w/+/b

#http://www.tutorialspoint.com/python/python_files_io.htm
#https://docs.python.org/2/tutorial/inputoutput.html


'''

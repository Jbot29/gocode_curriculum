
'''



Create a sample file using the .open() method. 
Code a loop that can write() 1000 lines of data to a sample file. Each line contains the line number of that line.

e.g.

1
2
3
4
5
6
'''

#create file here

'''

Goal: Write a program that splits a large file into two files based on line number.

The function will

- save the file's contents as a variable (consider what data type you want to use when you're splitting by line number later. array? string?)
- split the file at that line number you've given
- save 2 strings of the split file data
- write two new files out of those two strings with the orignal file name plus -1 or -2 appended to it. (e.g. filename-1.txt, filename-2.txt)


The filename-1.txt will have all the line numbers up to the number given.

The filename-2.txt will have all the line numbers > than the number given.

'''

# Here are some empty functions that are shown here as examples.  You do NOT have to use these if you don't want to.  You can create your own functions instead. It might be simpler to ignore the examples and to create your own logic rather than trying to use these.

def read_data(filename):
    pass

def write_data(filename,data):
    pass

def split_file(filename,line_number):
    pass

split_file("sample.txt",500)





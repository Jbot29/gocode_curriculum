
'''

Using what you've learned about defining classes, create a new class 
called FileHandler that will:

1) Take in a filename on initialization

fh = FileHandler("filename.txt")

It has two instance variables - filename and filedata

2) Parse the file using readlines and store it in an instance variable called filedata

You might want to create your own dummy text file to test this.

3) Has three methods:

i) A method that writes data to file and overwrites the original data

fh.write_new_data(data_in_array_format)

ii) A method that splits current file based on line_number passed into it.  

The first part of the file up to the line_number gets stored in the original file/filedata.

fh.split_file(line_number)

'''

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.filedata = filedata

    def write_data(self, data_array):
        pass

    def split_file(self):
    	pass

fh = FileHandler('filename.txt')
fh.write_new_data(["test","testdata"])



import string

"""
Content Indexing Engine Capstone Project

You have a bunch of files in the file system!  How can we index these files to make them easily searchable by keyword?

Indexing is a way of moving work 'upfront' so that when the user searches, less work is needed to get them the right search results.

Tips:

Look into array .extend() method
Look into string module , and .punctuation
Look into the set() builtin data type

Example index:
index = {'cat':['filename1','filename2','filename3'],'dog':['filename2',filename3]}

"""


#Tip: upgrade your recursive find code from a previous exercise to return a list of files 

def recursive_find(current_path):
    """recursive find all files and return a list of file names"""
    pass

stop_words = ['a','an','and','i']

def read_data(filename):
    with open(filename,"r") as f:
        return f.read()

def strip_punctuation(token):
    """strip out punctuation from a token"""
    pass

def index_file(filename):
    """Index one file return a cleaned array of words"""
    pass

        
def add_to_index(words,filename,index):
    """takes a set of words for a filename and adds it to the index"""
    pass

def index_all_files(file_list):
    """go through the list of files and add a file's words to the index and return a new index"""
    pass


def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    pass

            

        


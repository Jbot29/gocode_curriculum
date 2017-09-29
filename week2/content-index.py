import string

"""
Content Indexing Engine Capstone Project

You have a bunch of files in the file system!  How can we index these files to make them easily searchable by keyword?

Indexing is a way of moving work 'upfront' so that when the user searches, less work is needed to get them the right search results.

Tips:

Look into string module , and .punctuation
Look into the set() builtin data type

Example index:
index = {'cat':['filename1','filename2','filename3'],'dog':['filename2',filename3]}


Steps 

1) Pull in you recursive find code, and update it to return a list of all the files.
2) Fill out index_all_files. It takes the list of files, goes through each file and update the index, returning the entire index.
3) Fill out find_files_with, it takes the index, and list of keywords. It then returns a list of all the files that have that keyword in it. 

-Note when you index a file throwout all stop words.

"""

stop_words = ['a','an','and','i']

#Tip: upgrade your recursive find code from a previous exercise to return a list of files 

def recursive_find(current_path):
    """recursive find all files and return a list of file names"""
    pass


def index_all_files(file_list):
    """go through the list of files and add a file's words to the index and return a new index"""
    pass


def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    pass




        


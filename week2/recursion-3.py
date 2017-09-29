'''

Recursively walk a filesystem.

'''

import os


dirname = "."

# os.listdir(dirname) will give you an array of all the directories and files
array_all = os.listdir(dirname)
print array_all

# os.path.join(dirname, name) will combine a dirname (your root directory) and name (your folder inside your root) to create the path for that folder
path = os.path.join(dirname, os.listdir(dirname)[0])
print path

# os.path.isdir(path) will evaluate whether a certain path is a file or a directory
path = os.path.isdir(path)
print path


# write a function that takes in dirname and prints all the directories and files as well as prints subdirectories and files in all subdirectories. use recursion.
# tip: you can use for loops

#Trace through the algorithm to understand it
#Add print statements where appropriate so you can debug it easily

#Bonus: Create a directory with a bunch of sub-folders. Recursively delete all of them.  Make sure you don't do this on anything you need...
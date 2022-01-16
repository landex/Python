# This program verify is a directory exist and create a file and change permission.

# Importing the libraries.
from os import mkdir
from os import getcwd
from os import sys
import os

# Input name of directory.
print ('Please inform the directory that you can create!')
dir_name = input()

# Determine the directory structure that we will work.
# work_dir = '/Users/landileite/Programming/Python3/os_libs_testing'
work_dir = '~//Documents//Programming//python//head_first_pyhton//os_libs_testing/'

# Create a directory and access directory.
dir_to_create = os.path.join(work_dir, dir_name) 

# To verify is dir exist
dir_exist = os.path.exists(dir_to_create)

# Verify is directory exist, if not exist program exit.
if dir_exist == True:
    print ('This directory', dir_to_create + ' exist!!!')
    exit ()
else:
    print ('The directory', dir_to_create + ' will be created')
    os.mkdir(dir_to_create)

# List files in directory.
list_dir = os.path.dirname(dir_to_create)
print ('listing directory\n\n' + list_dir)

# Create an empty file in directory.
file_hi = open(dir_to_create + '/oi.txt','x')
print ('\n\noi.txt file was created')
# Insert data in file and list again.
print ('\n\n Now in the next lines system will be insert a data on text file!\n\n\n')

# Insert text in text file
file_hi = open (dir_to_create + '/oi.txt','w') 
file_hi.write ('Hello World') 
file_hi.write ('This is our new text file') 
file_hi.write ('and this is another line.') 
file_hi.write ('Why? Because we can.') 
file_hi.close () 

print ('\n\nFile was fill now!!! tks!')

print (os.listdir(dir_to_create)

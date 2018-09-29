# Python 3.6 - Windows 10.0.16299
# Noteclip: a simple program to get notes copied directly in the clipboard

import sys
import os

try:
    import pyperclip
except ImportError or ModuleNotFoundError:
    print('Pyperclip module not found. Please download it.')

try:
    note_name = sys.argv[1]
except IndexError:
    note_name = input('Please input the name of your note here: > ')

starting_dir = os.getcwd()
file_name = note_name + ".txt"
notes_path = 'C:\\Users\\Giuseppe\\Documents'

def find(file, path):
    for root, dirs, files in os.walk(path):
        if file in files:
            print (file +' found in ' + root)
            new_working_dir = root
            return new_working_dir
    else:
        print('There is no file called ' + file_name + ' in ' + path +
            '\nPlease make sure spelling and capitalisation are correct.')
        exit()

nwd = find(file_name, notes_path)

os.chdir(nwd)

def copy(the_file):
    file_text = open(the_file)
    content = file_text.read()
    pyperclip.copy(content)
    print('The content of ' + the_file + ' has been copied to the clipboard.')
    file_text.close()

copy(file_name)

os.chdir(starting_dir)

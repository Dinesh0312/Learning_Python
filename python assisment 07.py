
import os.path

file_exist = os.path.exists('abc.txt')
print(file_exist)

import os

directory = os.getcwd()

print(directory)

print(os.path.basename('abc.txt'))
print(os.path.isdir('abc.txt'))
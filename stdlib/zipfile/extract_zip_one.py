#!/usr/bin/python3

import zipfile

with zipfile.ZipFile('myfile.zip') as zf:
    
    zf.extract('todo.txt', 'extracted')

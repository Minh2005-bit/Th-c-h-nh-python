﻿print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")

def file_read(fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())

file_read('abc.txt')

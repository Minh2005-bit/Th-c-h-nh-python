print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)

file_read_from_head('D:/test.txt', 2)

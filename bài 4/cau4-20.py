﻿print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")


def pascal(n)
    row = [1]
    y = [0]
    for _ in range(max(n, 0)):
        print(row)
        row = [l+r for l, r in zip(row+y, y+row)]

n = int(input("Nhập số n: "))
pascal(n)


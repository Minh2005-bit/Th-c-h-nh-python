﻿print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")

binary_numbers = input("Nhập chuỗi các số nhị phân 4 chữ số: ").split(',')
divisible_by_5 = [bin_num for bin_num in binary_numbers if int(bin_num, 2) % 5 == 0]
print(",".join(divisible_by_5))

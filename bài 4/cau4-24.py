print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")
numbers = input("Nhập các số, phân tách bởi dấu phẩy: ").split(',')
odd_numbers = [num for num in numbers if int(num) % 2 != 0]
print(",".join(odd_numbers))

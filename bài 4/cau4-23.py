print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")

sentence = input("Nhập câu: ")
letters = sum(c.isalpha() for c in sentence)
digits = sum(c.isdigit() for c in sentence)
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")

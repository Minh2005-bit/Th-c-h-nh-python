print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")

even_digit_numbers = []
for number in range(1000, 3001):
    str_number = str(number)
    if all(int(digit) % 2 == 0 for digit in str_number):
        even_digit_numbers.append(str_number)

result = ",".join(even_digit_numbers)
print(result)

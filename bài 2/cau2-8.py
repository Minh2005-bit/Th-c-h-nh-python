print("Sinh Vien : NGO TRI MINH")
print("MSSV : 235752021610072")
a, b = 1, 2
total = 0
print(a, end=" ")
while (a <= 4000000-1):
    if a % 2 == 0:
        total += a
    a, b = b, a+b
    print(a, end=" ")
print("\n sum of even numbers in Fibonacci series: ", total)

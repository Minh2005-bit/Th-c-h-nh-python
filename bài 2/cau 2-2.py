print("Sinh Vien : NGO TRI MINH")
print("MSSV : 235752021610072")
import math

x1 = int(input("x1="))
y1 = int(input("y1="))

x2 = int(input("x2="))
y2 = int(input("y2="))

A = (x2 - x1) * (x2 - x1)
B = (y2 - y1) * (y2 - y1)

res = math.sqrt(A + B)
print("distance between two points:", res);

print("Sinh Vien : NGO TRI MINH")
print("MSSV : 235752021610072")
j = []
for i in range(680, 1500):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))

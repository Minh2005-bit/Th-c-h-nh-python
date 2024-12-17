print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")

def uoc_so(n):
    return [i for i in range(1, n) if n % i == 0]

n = int(input("Nhập số n: "))
ket_qua = [i for i in range(1, n) if sum(uoc_so(i)) > i]
print(ket_qua)

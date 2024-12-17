print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def area(self):
        return self.dai * self.rong

# Tạo một đối tượng Hinhchunhat với chiều dài 4 và chiều rộng 5
hinhchunhat = Hinhchunhat(4, 5)
print(hinhchunhat.area())

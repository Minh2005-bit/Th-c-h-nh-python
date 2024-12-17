print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")

class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng từ class Nam và Nu
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())

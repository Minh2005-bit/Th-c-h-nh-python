﻿print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")

# Mở tệp văn bản với chế độ đọc (r)
with open(r'C:\Users\woxih\OneDrive\Tài liệu\Zalo Received Files\a.txt', 'r', encoding='utf-8') as file:
    # Đọc toàn bộ nội dung tệp
    content = file.read()
    # In ra màn hình nội dung của tệp
    print(content)

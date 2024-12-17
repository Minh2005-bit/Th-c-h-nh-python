print("Sinh Vien :NGO TRI MINH")
print("MSSV :235752021610072")
# Nhap day cac tu tu ban phim
words = input("Nhap day cac tu: ").split()

# Sap xep tu theo thu tu tu dien
words_sorted = sorted(words)

# In ra cac tu theo thu tu tu dien
print(" ".join(words_sorted))

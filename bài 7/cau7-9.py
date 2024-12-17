print("Sinh Vien: NGO TRI MINH")
print("MSSV:235752021610072")

def copy_file_content(source_fname, dest_fname):
    with open(source_fname, 'r', encoding='utf-8') as source_file:
        with open(dest_fname, 'w', encoding='utf-8') as dest_file:
            for line in source_file:
                dest_file.write(line)

source_filename = 'abc.txt'
destination_filename = 'copy_abc.txt'
copy_file_content(source_filename, destination_filename)
print("PHAM PHUC HUNG : 64K2")

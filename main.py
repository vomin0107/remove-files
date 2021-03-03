import os

# 파일이 있는 폴더 경로
path = r'C:\Users\dir'

os_files = os.listdir(path)
print(os_files)
for dir in os_files:
    file_name = path + '/' + dir + '/file_name.txt'
    if os.path.isfile(file_name):
        os.remove(file_name)
        #os.rmdir(path, option) # remove directory


print('Done.')
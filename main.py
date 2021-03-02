import os

# 파일이 있는 폴더 경로
path = r'C:\Users\hong0\OneDrive - 주식회사 단후이\문서\LI\All_document\AI_고부과_과제\Source\annotation_type'

os_files = os.listdir(path)
print(os_files)
for dir in os_files:
    file_name = path + '/' + dir + '/README.roboflow.txt'
    if os.path.isfile(file_name):
        os.remove(file_name)
        #os.rmdir(path, option) # remove directory


print('Done.')

import os
import shutil
from_dir="Downloads"
to_dir="Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    print(name)
    print(extension)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=from_dir+'/'+filename
        path2=to_dir+'/'+"Image_files"
        path3= to_dir + '/' + "Document_Files" + '/' + filename
        print("path1",path1)
        print("path3",path3)
        if os.path.exists(path2):
            print("moving" + file_name +"....." )
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving"+filename + ".....")
            shutil.move(path1,path3)

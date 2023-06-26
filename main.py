import os

def fromto(path, new_path):
    
    #find all folders in the root folder
    fileList = os.listdir(path)
    f_name = os.path.basename(path)
    base = path.replace(os.path.basename(path),'')
    print(os.path.basename(base[:-1]))

    #move the file to save_folder
    for i in fileList:
        print('processing in '+i)
        if os.path.isfile(path+os.sep+i):
            os.rename(os.path.join(path, i), new_path + os.sep + os.path.basename(base[:-1]) + '-' + f_name + '-' + i)
        else:
            #find the possible folders in the folder and do recursion
            fromto(path + os.sep + i, new_path)

#get the folder path
path = input('path：')
fileList = os.listdir(path)

#create new save_folder for the files
new_path = path + '-save'

os.makedirs(new_path)
fromto(path, new_path)
exit = input()


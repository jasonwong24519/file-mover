# file-mover
move all of the files under a folder to another folder 

This program is used to move all files in a folder, including those in the folder under the user-provided folder.

To use the program, user needs to enter the path of the folder, for example:
```
C:\Users\(User_Name)\Desktop\(folder_name)
```
Then, the files will be moved to a new folder called:
```
C:\Users\(User_Name)\Desktop\(folder_name)-save 
```
To avoid duplicate file name, the files in the sub-folder will be renamed, like:
```
C:\Users\(User_Name)\Desktop\(folder_name)\(sub-folder_name)\(file_name)
```
become:
```
C:\Users\(User_Name)\Desktop\(folder_name)-save\(sub-folder_name)-(file_name)
```

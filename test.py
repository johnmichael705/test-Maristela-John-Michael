import os
import shutil

Files = input ("Input folder path: ")

if os.path.exists(Files):
    print("Changing path.")
else:
    print("no such folder")

list_of_files = os.listdir()
print(list_of_files)

count = 0
while count < 3:
    print(list_of_files, count)
for i in range(4):
    print(i)

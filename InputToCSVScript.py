import time
import os.path
from os import path
import shutil


def main():
    hospitalOrganizer = []
    str2 = ""
    if path.exists("testBackup.txt"):
        backupFile_object = open("testBackup.txt", "r")
        for x in backupFile_object:
            list1 = x.split(",")
            hospitalOrganizer.append(list1)
    while True:
        pointer = 0
        f = open("testInput.txt", "r")
        str1 = f.read()
        if str1 != "":
            if str1 != str2:
                my_list = str1.split(",")
                hospital = my_list[0]
                exists = False
                count = 0
                for i in hospitalOrganizer:
                    if i[0] == hospital:
                        exists = True
                        pointer = count
                    count += 1
                if exists:
                    print(hospitalOrganizer[pointer][0])
                    print(hospitalOrganizer[pointer][1])
                    print(hospitalOrganizer[pointer][2])
                    print(hospitalOrganizer[pointer][3])
                    print(my_list[1])
                    print(my_list[2])
                    print(my_list[3])
                    # number of submitted
                    hospitalOrganizer[pointer][1] = hospitalOrganizer[pointer][1] + my_list[1]
                    # number of good hit
                    hospitalOrganizer[pointer][3] = hospitalOrganizer[pointer][2] + my_list[2]
                    # number of no hit
                    hospitalOrganizer[pointer][3] = hospitalOrganizer[pointer][3] + my_list[3]
                    File_object = open("testOutput.txt", "w")
                    #TODO remove trailing comma because it makes an empty entry
                    for i in hospitalOrganizer:
                        #i = map(lambda v: v + ',', i)
                        #File_object.writelines(i)
                        my_string = ','.join(map(str, i))
                        File_object.writelines(my_string)
                        File_object.write('\n')
                    File_object.close()
                    shutil.copyfile("testOutput.txt", "testBackup.txt")
                else:
                    hospitalOrganizer.append(my_list)
                    File_object = open("testOutput.txt", "w")
                    for i in hospitalOrganizer:
                        #i = map(lambda v: v + ',', i)
                        #File_object.writelines(i)
                        my_string = ','.join(map(str, i))
                        File_object.writelines(my_string)
                        File_object.write('\n')
                    File_object.close()
                    shutil.copyfile("testOutput.txt", "testBackup.txt")

                str2 = str1
                time.sleep(1)
            else:
                time.sleep(1)


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)


if __name__ == "__main__":
    main()

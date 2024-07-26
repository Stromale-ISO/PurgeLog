#!/bin/python3
# ---------------------------------------------------
# Program by Roman.
#
#
# Version        Date         Info
# 1.0            2024      Test Version
# ---------------------------------------------------
import shutil # Чтобы копировать файлы
import os     # Чтобы узнать размер файла и проверять его существование
import sys    # Инструменты для аргументов командной строки

# PurgeLog.py mylog.txt 10 5 (наш скрипт, файл логов, сколько максимум КБ, сколько файлов)
# PurgeLog.py   mylog.txt   10   5    (наш скрипт, файл логов, сколько максимум КБ, сколько файлов)

if(len(sys.argv) < 4):
    print("Недостаточно аргументов")
    exit(1)


file_name = sys.argv[1]
limitsize = int(sys.argv[2])
#logsnumber
#Potom dodelayu
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):         # проверка существует ли файл
    logfile_size = os.stat(file_name).st_size  # получение размера файла в Байтах
    logfile_size = logfile_size / 1024         # конвертируем в килобайты
    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber , 1, -1):
                src = file_name + "_" + str(currentFileNum - 1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src)  == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "     to " + file_name + "_1")
        myfile = open(file_name, "w")
        myfile.close()

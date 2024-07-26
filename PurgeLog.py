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

if(len(sys.argv) < 4):
    print("Недостаточно аргументов")


file_name = sys.argv[1]
limitsize = int(sys.argv[2])
#logsnumber
#Potom dodelayu

"""
# Powered by FZZkill
# Code with Neovim
# Project: Qython
# author: FZZkill
# License: Mozilla Public License 2
"""
import os

class IoUtil :

    def __eq__(this, obj) :
        return True
    def __bool__(this) :
        ...

    strToLs = lambda this, Items : list(Items)
    lsToStr = lambda this, Items : "".join(Items)
    lsToStrRN = lambda this, Items : "\n".join(Items)

    def strToLsesRN(this, Items : str) :
        im = Items.split("\n")
        x = []
        for i in im:
            for j in range(len(i)-1):
                if str(i[j]) + str(i[j+1]) == "\n" :
                    break
                x.append(i[j])
        return x

def readInList(FilePath) :
    with open(FilePath, 'r') as f :
        return f.readlines()

def readInString(FilePath) :
    with open(FilePath, 'r') as f :
        return f.read()

def write(Items, FilePath) :
    with open(FilePath, 'w') as f:
        f.write(FilePath)

def writeInList(Items, FilePath):
    RN = IoUtil.lsToStrRN(Items)
    with open(FilePath, 'w') as f:
        f.write(RN)

def isFile(FilePath) :
        return os.path.isfile(FilePath)

import os
import random


class Util:
    def __init__(self):
        self.command = "python marker.py -f "

    def addWaterMark(self,path,mark):
        print(self.command + path+ " -m "+mark)
        os.system(self.command + path+ " -m "+mark)

    def randString(self,length):
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(length):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        return salt

    def randRenameFiles(self,rootPath):
        fileNames = []
        for _, _, files in os.walk(rootPath):
            for eachName in files:
                fileNames.append(rootPath + eachName)
        for imgName in fileNames:
            fileType = imgName.split('.')[-1]
            os.rename(imgName,rootPath+self.randString(12)+'.'+fileType)
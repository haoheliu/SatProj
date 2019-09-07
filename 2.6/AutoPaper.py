import datetime
import matplotlib.pyplot as plt
import tkinter.messagebox
import tkinter

from tkinter import *
from Config import *
from Util import *

global config
config = ConfigObject()
util = Util()

'''
1. Rename files
2. Modify file name
3. Add watermarks
4. Randomly rename ,Rebase system
5. statics
6. Tinker GUI
7. ERROR spot
'''
def fileName(rootDir) -> list:
    fileNames = []
    for _, _, files in os.walk(rootDir):
        for eachName in files:
            fileNames.append(rootDir + eachName)
    return fileNames

def processFiles(fileName):
    '''
    :param fileName: the filenames to be processed
    :return: void
    '''
    now = datetime.datetime.now().strftime('%Y_%m_%d_')
    for imgName in fileName:
        fileType = imgName.split('.')[-1]
        if(not fileType in config.fileType):
            if(len(config.fileType) == 0):
                pass
            else:
                continue
        config.counter[fileType] += 1
        os.rename(imgName,config.rootDir+config.imgRootName+fileType+"File"+now+str(config.counter[fileType]).zfill(config.zfillVal)+'.'+fileType)
    print(config.counter)

def addWaterMark(modifiedImgNames):
    '''
    :param modifiedImgNames: for each png file , add watermark
    :return: void
    '''
    for fname in modifiedImgNames:
        fileType = fname.split('.')[-1]
        if(fileType == 'png'):
            util.addWaterMark(fname,config.waterMark)

def report():
    '''
    :return: pie chart
    '''
    plt.figure(figsize=(6,12))
    labels = config.counter.keys()
    sizes = config.counter.values()
    plt.pie(sizes,labels=labels,autopct='%1.2f%%',shadow=True)
    plt.title("File name statics")
    plt.axis('equal')
    plt.show()

def massageBox():
    root = Tk()
    Label(root,text="请输入文件头：").grid(row = 0,column =0)
    Label(root,text="#的个数：").grid(row = 1,column =0)
    Label(root,text="文件类型：").grid(row = 2,column =0)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e1.grid(row =0 ,column =1)
    e2.grid(row =1 ,column =1)
    e3.grid(row =2 ,column =1)

    def confirm():
        if(len(e1.get()) == 0):
            tkinter.messagebox.showerror('错误','文件头不能为空')
        elif(not e2.get().isdigit()):
            tkinter.messagebox.showerror('错误','#的个数必须为数字')
        else:
            choice = True
            if(len(e3.get()) == 0):
                choice = tkinter.messagebox.askyesno('提示',"确定应用于所有文件类型吗")
                if(choice == False):
                    return
            config.imgRootName = e1.get()
            config.zfillVal = int(e2.get())
            if(len(e3.get()) != 0 and choice == False):
                config.fileType = str(e3.get()).split(" ");
            choice = tkinter.messagebox.askyesno('提示', '要执行此操作吗?'+"\n文件头: "+config.imgRootName+"\n编号长度: "+str(config.zfillVal))
            if(choice == True):
                root.quit()

    def dele():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
    theButton1 = Button(root, text ="执行", width =10,command =confirm)
    theButton2 = Button(root, text ="清除",width =10,command =dele)
    theButton1.grid(row =3 ,column =0,sticky =W, padx=10,pady =5)
    theButton2.grid(row =3 ,column =1,sticky =E, padx=10,pady =5)
    mainloop()

if __name__ == '__main__':
    massageBox()
    imgNames = fileName(config.rootDir)
    processFiles(imgNames)
    modifiedImgNames = fileName(config.rootDir)
    choice = tkinter.messagebox.askyesno('提示', '要为所有png图片添加水印吗?')
    if(choice == True):
        addWaterMark(modifiedImgNames)
    report()
    util.randRenameFiles(config.rootDir)

from collections import defaultdict

class ConfigObject:
    def __init__(self):
        self.rootDir = './imgCache/'
        self.imgRootName = None     #指定根文件名
        self.zfillVal = None        #指定填充长度
        self.waterMark = '刘濠赫'  #可以添加文字水印
        self.counter = defaultdict(lambda : 0)
        self.fileType = []   #可以执行文件类型

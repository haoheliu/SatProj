from collections import defaultdict
import matplotlib.pyplot as plt
import re

alphaFrequency = defaultdict(lambda : 0)

def isalpha(chr):
    '''
    :param chr: A char
    :return: True / False equal to the function of str.isalpha()
    '''
    if(ord(chr) < ord('z') and ord(chr) > ord('a') or ord(chr) < ord('Z') and ord(chr) > ord('A')):
        return True
    else:
        return False

def isAlphaStr(str):
    for each in str:
        if(str == 'According'):
            print(each)
        if(not each.isalpha()):
            return False
    return True

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


allText = open('dataSource').read()
li = allText.split(" ")

for each in li:
    if(isChinese(each) or not isAlphaStr(each)):
        li.remove(each)
    else:
        alphaFrequency[each] += 1

for each in alphaFrequency.keys():
    alphaFrequency[each] /= sum(alphaFrequency.values())

for each in alphaFrequency.keys():
    print(each,alphaFrequency[each])

plt.xlabel("Alphas")
plt.ylabel("Frequency")
plt.bar(alphaFrequency.keys(),alphaFrequency.values())
plt.savefig("freq.png")
plt.show()

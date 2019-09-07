from collections import defaultdict
import matplotlib.pyplot as plt
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

with open("dataSource",'rb') as f:
    for each in f.readline():
        if(isalpha(chr(each))):
            alphaFrequency[chr(each)] += 1

for each in alphaFrequency.keys():
    alphaFrequency[each] /= sum(alphaFrequency.values())

for i in range(0, 25):
    print(chr(ord('A') + i), alphaFrequency[chr(ord('A') + i)])

plt.xlabel("Alphas")
plt.ylabel("Frequency")
plt.bar(alphaFrequency.keys(),alphaFrequency.values())
plt.savefig("freq.png")
plt.show()


#!/usr/bin/python3

import os
import sys
import re

args = sys.argv
filePath = args[1]
fileRaw = open(filePath, 'rb')
fileNew = open("result_file4.txt",'w',encoding='utf-8')


'''for lines in fileRaw.readlines():
    line = str(lines.strip())
    #line = str(lines.strip().decode('utf-8'))
    #line = str(lines.decode('gb18030','ignore'))
    print(line)
    temp = str(re.search('[a-zA-Z]+',line))
    print(len(temp))

    if((1 <= len(temp)) and (len(temp) <= 4)):
        print(line)
        fileNew.write(line + '\n')'''



'''lines = fileRaw.read().decode('utf-8')
lines = str(lines).split('\n')
for line in lines:
    #line = str(lines.strip().decode('utf-8'))
    #line = str(lines.decode('gb18030','ignore'))
    print(line)
    temp = str(re.search('[a-zA-Z]+',line))
    print(len(temp))

    if((1 <= len(temp)) and (len(temp) <= 4)):
        print(line)
        fileNew.write(line + '\n')'''



lines = fileRaw.read().decode('utf-8')
lines = str(lines).split('\n')
for line in lines:
    #line = str(lines.strip().decode('utf-8'))
    #line = str(lines.decode('gb18030','ignore'))
    #print(line)
    temp = str(re.search('\w+',line).group())
    #print(len(temp))

    #if((11 <= len(temp)) and (len(temp) <= 12)):
    if(13 <= len(temp)):
        #print(line)
        fileNew.write(line + '\n')


fileRaw.close()
fileNew.close()






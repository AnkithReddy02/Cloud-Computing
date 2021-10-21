#!/usr/bin/python3
import sys

classNum = None
lis = None
count = 0

for line in sys.stdin:
    line=line.strip().split(',')
    currClassNum=line[0]
    currLis = [float(line[i]) for i in range(1,len(line))]


    if classNum == None:
        classNum = currClassNum
        lis = currLis
        count = 1
    elif classNum == currClassNum:
        lis = [x+y for x,y in zip(lis,currLis)]
        count += 1
    else :
        lis = [x/count for x in lis]
        print(f'{classNum},{lis[0]},{lis[1]},{lis[2]},{lis[3]}')

        lis = currLis
        count = 1
        classNum = currClassNum


print(f'{classNum},{lis[0]/count},{lis[1]/count},{lis[2]/count},{lis[3]/count}')
        

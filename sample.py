#!/usr/bin/env python

from string import digits
from random import randint, choice

count = 0

print ("""random number to play 2A1B""")


numStr = '0123456789'
randNum = ''
for i in range(4) :
    n = choice(numStr)
    randNum = randNum + n
    numStr = numStr.replace(n, '')

#print ('Debug >> randNum',randNum)



def isallnumber(num):
    for ch in num :
        if ch not in digits :
            return False
    return True

def hasSameDigit(sameNum) :
    for i in range(len(sameNum)):
        if (sameNum[0]==sameNum[1]) or (sameNum[0]==sameNum[2]) or (sameNum[0]==sameNum[3]) or (sameNum[1]==sameNum[2]) or (sameNum[1]==sameNum[3]) or (sameNum[2]==sameNum[3]):
            return True
    return False
    
userNums = []    
results = []

Winner = 0
while Winner == 0:

    num = []
    number = 0
    while (number == 0):
        num = input('infput four number')
        if (isallnumber(num) == False) :
            print ('***wrong:not number')
            exit
        elif (hasSameDigit(num) == True):
            print ('***wrong:please input different number')
        elif (len(num) != 4) :
            print ('***wrong pleae input four number')
            exit
            
        else:
            number +=1
    userNum = num
    userNums.append(userNum)
    #print ('Debug >> userNum',userNum)

    seatA = 0 
    seatB = 0
    count +=1
    for i in range(4) :
        if userNum[i] in randNum :
            if i == randNum.find(userNum[i]) :
                seatA += 1
            else :
                seatB += 1
        if seatA == 4:
            print ("you win!!")
            Winner = 1
        else:
            exit
        result = '%dA%dB' % (seatA, seatB)
    results.append(result)


    print ('-' * 20)

    for i in range(count) :
        print ('(%d)/%s/%s' % (i + 1, userNums[i], results[i]))
    print ('-' * 20)
    if Winner == 1 :
        print ('Total: %d times' % count)
        print ('Congratulations Your are winner')

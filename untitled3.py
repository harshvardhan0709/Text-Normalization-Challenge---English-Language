#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 03:38:56 2017

@author: harsh
"""

ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]

ByTen = [
"zero",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

zGroup = [
"",
"thousand",
"million",
"billion",
"trillion",
"quadrillion",
"quintillion",
"sextillion",
"septillion",
"octillion",
"nonillion",
"decillion",
"undecillion",
"duodecillion",
"tredecillion",
"quattuordecillion",
"sexdecillion",
"septendecillion",
"octodecillion",
"novemdecillion",
"vigintillion"
]

# A recursive function to get the word equivalent for numbers under 1000.











def subThousand(inputNum):
    num = int(inputNum)
    if 0 <= num <= 19:
        return ByOne[num]
    elif 20 <= num <= 99:
        if inputNum[-1] == "0":
            return ByTen[int(inputNum[0])]
        else:
            return ByTen[int(inputNum[0])] + "-" + ByOne[int(inputNum[1])]
    elif 100 <= num <= 999:
        rem = num % 100
        dig = num / 100
        if rem == 0:
            return ByOne[dig] + " hundred"
        else:
            return ByOne[dig] + " hundred and " + subThousand(str(rem))

# A looping function to get the word equivalent for numbers above 1000
# by splitting a number by the thousands, storing them in a list, and 
# calling subThousand on each of them, while appending the correct
# "zero-group".

def thousandUp(inputNum):
    num = int(inputNum)
    arrZero = splitByThousands(num)
    lenArr = len(arrZero) - 1
    resArr = []
    for z in arrZero[::-1]:
        wrd = subThousand(str(z)) + " "
        zap = zGroup[lenArr] + " "
        if wrd == " ":
            break
        elif wrd == "zero ":
            wrd, zap = "", ""
        resArr.append(wrd + zap)
        lenArr -= 1
    res = "".join(resArr).strip()
    if res[-1] == ",": res = res[:-1]
    return res

# Function to return a list created from splitting a number above 1000.

def splitByThousands(inputNum):
    num = int(inputNum)
    arrThousands = []
    while num != 0:
        arrThousands.append(num % 1000)
        num /= 1000
    return arrThousands

for i in range(len(l1)):
    l3.append(str(l1[i])+"_"+str(l2[i]))
    
l4=list(test["before"])
PATTERN = r"([A-Z]{2}\w+)"
PATTERN2 = r"\d+"
PATTERN3 = r"\w+"

l5=[]
for i in range(len(l4)):
    digits = re.search(PATTERN2, l4[i])
    ls = re.search(PATTERN, l4[i])
    if( None == ls):
        if( None == digits):
            l5.append(l4[i])
        else:
            list_digit=l4[i].split()
            for i in range(len(list_digit)):
                status_digit=list_digit[i].isdigit()
                if(status_digit == True):
                    strNum = list_digit[i]
                    intNum = int(list_digit[i])
                    print(strNum)
             
                else:
                    print(list_digit[i])
            l5.append(l4[i])
    else:
        l5.append(l4[i])
        #l6=list(l4[i])
        #te = ""
        #for a in range(len(l6)):
        #    te = te+str(l6[a])+" "
        #print(te)

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isAlternated(s):
    if len(s) < 2:
        return False
    
    first = s[0]
    second = s[1]
    
    if first == second:
        return False
    
    f = True
    for c in s[2:]:
        if f:
            if c != first:
                return False
            else:
                f = not f
        else:
            if c != second:
                return False
            else:
                f = not f
                
    return True             

def alternate(s):
    # Write your code here
    possibleChar = {}
    for c in s:
        if c not in possibleChar:
            possibleChar[c] = 1
        else:
            possibleChar[c] += 1
            
    possChar = possibleChar.keys()
    allCombinations = list(itertools.combinations(possChar,2))
    
    maxLen = 0
    for first,second in allCombinations:
        if abs(possibleChar[first] - possibleChar[second]) <= 1:
            newS = s
            
            for c in list(filter(lambda c: c != first and c != second,possChar)):
                newS = newS.replace(c,"")
            
            if isAlternated(newS) and len(newS) > maxLen:
                maxLen = len(newS)
                
    return maxLen
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

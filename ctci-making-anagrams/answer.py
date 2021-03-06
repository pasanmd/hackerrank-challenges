#!/bin/python3

import math
import os
import random
import re
import sys
import string


module_path = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH = '/home/pasanmd/hackerrank/ctci-making-anagrams/result.txt'
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_list = strngtolst(ascii_lowercase)
    #ascii_list = list(string.ascii_lowercase)
    finxtracnt = 0
    for i in range(len(ascii_list)):
        xtracnt = stringCharXtraFreq(a, b, ascii_list[i])
        finxtracnt = finxtracnt + xtracnt
    return finxtracnt




def strngtolst(a):
    list1=[]
    list1[:0]=a
    return list1


def stringCharXtraFreq(a, b, char):
    cnt1 = a.count(char)
    cnt2 = b.count(char)
    xtrachar = 0
    if cnt1 > cnt2:
        xtrachar = cnt1 - cnt2
        return int(xtrachar)
        print (xtrachar)
    elif cnt1 < cnt2:
        xtrachar = cnt2 - cnt1
        return int(xtrachar)
        print (xtrachar)
    else:
        return  int(xtrachar)
        print (xtrachar)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input("Enter the first string")
    b = input("Enter the Second String")

    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()

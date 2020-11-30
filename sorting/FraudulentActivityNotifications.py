#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left, insort_left
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    noti = 0
    n = len(expenditure)
    listD = sorted(expenditure[:d])

    def median():
        return listD[d//2] if d%2 == 1 else ((listD[d//2] + listD[d//2-1])/2)

    for i in range(d,n):
        if expenditure[i] >= 2*median(): noti += 1
        del listD[bisect_left(listD, expenditure[i-d])]
        insort_left(listD, expenditure[i])
    return(noti)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

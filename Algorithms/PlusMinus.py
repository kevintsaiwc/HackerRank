#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_sum, neg_sum, zero_sum = 0, 0, 0
    n = len(arr)
    for i in arr:
        if i > 0:
            pos_sum = pos_sum + 1
        elif i < 0:
            neg_sum = neg_sum + 1
        else:
            zero_sum = zero_sum + 1
    pos_sum = pos_sum / n
    neg_sum = neg_sum / n
    zero_sum = zero_sum / n
    print(f"{pos_sum:.6f}")
    print(f"{neg_sum:.6f}")
    print(f"{zero_sum:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

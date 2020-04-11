#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    #n =100
    print(n)

    if (n % 2 != 0):
        print("Weird")
    elif(n%2 ==0 and n in range(6,20)):
        print("weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    main()

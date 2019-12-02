import math
import os
import random
import re
import sys

n = int(input())

if 1 <= n <= 100 and n % 2 == 1:
    print("Weird")
else:
    if 1 <= n <= 100 and 2 <= n <= 5:
        print("Not Weird")
    elif 1 <= n <= 100 and 6 <= n <= 20:
        print("Weird")
    elif 1 <= n <= 100 and n >= 20:
        print("Not Weird")

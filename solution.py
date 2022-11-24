from collections import *
from math import *

def getInversions(arr, n) :
	# Write your code here.
    c=0
    for i in range(n):
      for j in range(n):
         if (arr[i]>arr[j]) and i<j:
           c+=1
    return(c) 

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))

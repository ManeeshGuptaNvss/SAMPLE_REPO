import os
import sys
size=int(input())
str1=input()
arr= map(int,str1.split() )
lis1=list(arr)

lis1.sort()
max_product=(lis1[-1])*(lis1[-2])*(lis1[-3])
print(max_product)
    
    

import sys
import math
from fractions import Fraction
input= sys.stdin.readline

lst= []
rstlst= []
cnt= int(input())

for i in range(cnt):
    lst.append(list(map(int, input().split())))

for i in range(cnt):
    sum=0
    lcm= math.lcm(lst[i][1], lst[i][2], lst[i][3])

    for j in range(1, 4):
        sum+=Fraction(1, lst[i][j])

    q= sum.numerator
    p= sum.denominator
    q = q * (lcm/p)
    p = lcm

    if q>p:
        rstlst.append(-1)
    else:
        n= lst[i][0]
        if(n%q==0):
            p2= p*(n/q)
            p2-=n
            rstlst.append(int(p2))
        else:
            rstlst.append(-1)

print('\n'.join(map(str, rstlst)))

"""
4
17 2 3 9
9 3 3 3
10 2 4 6
15 2 3 4
"""
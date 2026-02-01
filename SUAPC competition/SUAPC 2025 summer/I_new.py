import sys
input= sys.stdin.readline

n= int(input())
s= list(input())

h= s.count("H")
cnt=0

def findH3(s, start):
    a=[-1, -1]
    count = 0
    for i in range(start, len(s)):
        if s[i]=="H":
            if a[1] == 1:
                return count-2
            elif a[0] == 1 and a[1] == 0:
                a[1] = 1
            else:
                a[0] = 1
                a[1] = 0
        else:
            a[0]=0
            a[1]=0
            
        count = count+1
    return -1

def findH5(s):
    a=[-1, -1, -1, -1]
    count = 0
    for i in s:
        if i=="H":
            if a[3] == 1:
                return count-4
            elif a[2] == 1 and a[3] == 0:
                a[3] = 1
            elif a[1] == 1 and a[2] == 0:
                a[2] = 1
                a[3] = 0
            elif a[0] == 1 and a[1] == 0:
                a[1] = 1
                a[2] = 0
                a[3] = 0
            else:
                a[0] = 1
                a[1] = 0
                a[2] = 0
                a[3] = 0
        else:
            a[0]=0
            a[1]=0
            a[2]=0
            a[3]=0
            
        count = count+1
    return -1

if findH5(s)!=-1:
    r="First"
else:
    idx = 0
    while True:
        idx= findH3(s, idx)
        if idx==-1:
            break
        s[idx+1]="T"
        idx = idx+2
        cnt+=1

    if (h%2==1 and cnt%2==0) or (h%2==0 and cnt%2==1):
        r="First"
    else:
        r="Second"

print(r)

"""
9
HHHTHHHTH
"""
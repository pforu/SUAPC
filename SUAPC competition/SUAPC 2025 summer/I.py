import sys
input= sys.stdin.readline

n= int(input())
s= list(input())
cnt=0

k=s.count("H")%2


def findHHH(s):
    a=[-1, -1]
    count = 0
    for i in s:
        if i=="H":
            if a[1] == 1:
                return count
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



for i in range(n):
    idx_h= findHHH(s)
    if idx_h==-1:
        if k==0:
            rst="Second"
        else:
            rst="First"
    else:
        s[idx_h+1]= "T"
        cnt+=1


if k==1:
    if cnt%2==0:
        rst="First"
    else:
        rst="Second"
else:
    rst="Second"

print(rst)
import sys
input= sys.stdin.readline

t= int(input())
rstlst=[]

for i in range(t):
    n= int(input())
    lst= list(map(int, input().split()))
    r=[-1, -1]

    if n==2:
        if lst[0]>lst[1]:
            r[0]= 1
            r[1]= 2
    
    else:
        flag=0

        bool1= lst[0]<lst[2]
        bool2= lst[0]>lst[1]
        if bool2 and bool1:
            flag=1
            r[0]= 1
            r[1]= 2

        bool1= lst[n-3]<lst[n-1]
        bool2= lst[n-2]>lst[n-1]
        if bool2 and bool1:
            flag=1
            r[0]= n-1
            r[1]= n

        if flag==0:
            for j in range(n-3):
                bool1= lst[j]<lst[j+2]
                bool2= lst[j+2]<lst[j+1]
                bool3= lst[j+1]<lst[j+3]
                if bool2 and bool1 and bool3:
                    r[0]= j+2
                    r[1]= j+3
                    break

    if r[0]==-1:
        rstlst.append(-1)
    else:
        rstlst.append(f"{r[0]} {r[1]}")

print('\n'.join(map(str, rstlst)))
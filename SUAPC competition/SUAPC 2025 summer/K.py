import sys
input= sys.stdin.readline

lst=[]
t= int(input())
rstlst=[0]*t
for _ in range(t):
    lst.append(list(map(int, input().split())))

idx=0
for x, n in lst:
    numlst=[]
    for i in range(x+2*n-1, x-1, -1):
        numlst.append(i)
    
    for c in range(x, x+n+1):
        iflst=[]
        iflst.append(x+2*n)
        iflst.append(c)
        flag=1
        for i in numlst:
            if i not in iflst:
                iflst.append(i)
                if i-c not in iflst:
                    iflst.append(i-c)
                else:
                    flag=0
                    break
            else:
                flag=0
                break

        if flag==1:
            rstlst[idx]+=1
            
    idx+=1

print('\n'.join(map(str, rstlst)))
import sys
input= sys.stdin.readline

n, x= map(int, input().split())

info= [[0]*6]*(n+1)
for i in range(1, n+1):
    info[i]= [0]+list(map(int, input().split()))
        
q= int(input())
question= []
for i in range(q):
    question.append(list(map(int, input().split())))


routes= []
stop= [[0]*6]*(n+1)

def transfer(start, end, route):

    if start==end:
        routes.append(route)
        return
    
    for i in range(1, 6):
        line= info[start][i]

        for j in range(1, n+1):
            if line==info[j][i] and j!=start and stop[j][i]==0: #같은 노선에 존재, 자기가 아님, 방문 안 함 
                stop[start][i]=1
                transfer(j, end, route+1)
                stop[start][i]=0

    min_transfer= min(routes) if len(routes)!=0 else -1
    return min_transfer


rst=[]
for u, v in question:
    rst.append(transfer(u, v, 0))
    routes=[]

print('\n'.join(map(str, rst)))
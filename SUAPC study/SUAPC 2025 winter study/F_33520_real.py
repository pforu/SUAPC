'''
N = int(input())
choco=[]
choco_length=[]
choco_width=[]
mold_length=0
mold_width=0

for i in range(N):
    n, m= map(int, input().split())
    choco.append((n, m))
    choco_length.append((n, i))
    choco_width.append((m, i))

choco_length.sort(key=lambda x: x[0], reverse=True)
choco_width.sort(key=lambda x: x[0], reverse=True)

for i in range(N):
    if choco_length < mold_length and choco_length < mold_width:
        if choco_width < mold_length and choco_width < mold_width:
            break
        else:
'''

N = int(input())
choco_max_side=[]
choco_min_side=[]

for i in range(N):
    n, m= map(int, input().split())
    choco_max_side.append(max(n, m))
    choco_min_side.append(min(n, m))

max_length1= max(choco_max_side)
max_length2= max(choco_min_side)

print(max_length1*max_length2)
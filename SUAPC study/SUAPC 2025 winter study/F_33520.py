#import time

N = int(input())
choco=[]
choco_pair=[]
choco_selected=[0]*N
mold=[0, 0]
total_area= 0

for i in range(N):
    n, m= map(int, input().split())
    total_area += n*m
    choco.extend([(n, i, 0), (m, i, 1)])
    choco_pair[i]= (n, m)

#time_start= time.time() #####################################################
choco.sort(key=lambda x: x[0], reverse=True)

selection_cnt=0
mold_area= 0
for length, idx_out, idx_in in choco:
    mold_area= mold[0]*mold[1]
    if  mold_area > total_area:
        break
    if idx_out in choco_selected:
        continue
    mold[idx_in] += length
    mold[~idx_in] += choco_pair[idx_out][~idx_in]
    choco_selected.append(idx_out)
    choco
    selection_cnt != selection_cnt

print(mold_area)


#time_end= time.time() #######################################################
#print(time_end - time_start)
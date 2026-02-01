import sys
input = sys.stdin.readline

length= int(input())
string= list(input())

P_idx= []
C_idx= []

for i in range(length):
    if string[i]=='P':
        P_idx.append(i)
    if string[i]=='C':
        C_idx.append(i)

max_idx= min(len(P_idx), len(C_idx))

cnt=1
for i in P_idx:
    if cnt>max_idx:
        break
    string[i]= 'C'
    cnt+=1

cnt=1
for i in C_idx:
    if cnt>max_idx:
        break
    string[i]= 'P'
    cnt+=1

print(''.join(map(str, string)))
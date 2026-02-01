"""
import sys
import math
input= sys.stdin.readline

N=int(input())
t=list(map(int, input().split())) #상태 
K=int(input())
s=list(input()) #메크로 
c=0 #t에서 도는 상태 변수 인덱스 -> 지금 위치, j 시 증가, next로 상태 변화 가능 
until= 0
flag=0 #0:no, 1:yes

print()

while True:
    i=0 #s에서 도는 메크로 변수 인덱스 -> 무조건 증가, until이 끝날 때까지 처음으로 돌아감 

    while True:
        if c==N-1: #내가 징검다리 끝까지 감
            print("YES")
            flag=1
            break

        if until== math.pow(10, 100): #메크로가 최대로 돌았음 
                print("최대반복")
                print("NO")
                flag=1
                break

        if i==K: #메크로가 한 바퀴 돌았음
            break

        if next==0:
            if s[i]=="J":
                c+=1
                print("빈칸, 점프")
            print("빈칸, 점프안함")
        
        elif next==-1:
            if s[i]=="J":
                c+=1
                print("지뢰, 점프, 종료")
                print("NO")
                flag=1
                break

            elif s[i]=="D":
                next==0
                print("지뢰, 제거")

        elif next>=1:
            if s[i]=="J":
                c+=1
                print("곰, 점프, 종료")
                print("NO")
                flag=1
                break

            elif s[i]=="A":
                next-=1
                print(f"곰, 공격, 곰 체력: {next}")

        i+=1
        until+=1

    if flag==1:
        break
"""

"""
import sys
input= sys.stdin.readline

N=int(input())
t=list(map(int, input().split())) #상태 
K=int(input())
s=list(input()) #메크로 
c=0 #t에서 도는 상태 변수 인덱스 -> 지금 위치, j 시 증가, next로 상태 변화 가능 
i=0 #s에서 도는 메크로 변수 인덱스 -> 무조건 증가, 계속 처음으로 돌아감 

print()

while True:
    if "J" not in s: #못 감 애초에 
        print("NO")
        break

    if c==N-1: #내가 징검다리 끝까지 감
        print("YES")
        break

    if i==K: #메크로가 한 바퀴 돌았음
        i=0

    next= t[c+1]

    if next==0:
        if s[i]=="J":
            c+=1
            print(f"위치 {c}, 메크로 {i}: 빈칸, 점프")
            i+=1
    
    elif next==-1:
        if s[i]=="J":
            c+=1
            print(f"위치 {c}, 메크로 {i}: 지뢰, 점프, 종료")
            print("NO")
            break

        elif s[i]=="D":
            next=0
            print(f"위치 {c}, 메크로 {i}: 지뢰, 제거")
            i+=1

    elif next>=1:
        if s[i]=="J":
            c+=1
            print(f"위치 {c}, 메크로 {i}: 곰, 점프, 종료")
            print("NO")
            break

        elif s[i]=="A":
            next-=1
            print(f"위치 {c}, 메크로 {i}: 곰, 공격, 곰 체력: {next}")
            i+=1

    i+=1"""

import sys
input= sys.stdin.readline

N=int(input())
t=list(map(int,input().split()))
K=int(input())
s=input()
c=0
a=1

if "J" in s:
    while a:
        for i in s:

            if t[c+1]==0:
                if i=="J":
                    c+=1
                    if c==N-1:
                        print("YES")
                        a=0
                        break

            elif t[c+1]==-1:
                if i=="J":
                    print("NO")
                    a=0
                    break
                elif i=="D":
                    t[c+1]=0
                    
            elif t[c+1]>=1:
                if i=="J":
                    print("NO")
                    a=0
                    break
                elif i=="A":
                    t[c+1]-=1
else:
    print("NO")
import sys
import bisect

def bisearch(max_solve):
    left, right= 1, 300000
    while left<right:
        mid= (left + right +1) //2
        if 3*mid*(mid-1)+1 <= max_solve:
            left= mid
        else:
            right= mid-1
    return left

input = sys.stdin.readline

question_num, people_num = map(int, input().split())
question_level= list(map(int, input().split()))
people_skill= list(map(int, input().split()))

question_level.sort()

rst=[]
for skill in people_skill:
    max_solve= bisect.bisect_right(question_level, skill)
    if max_solve==0:
        rst.append(0)
    else:
        rst.append(bisearch(max_solve))

print(' '.join(map(str, rst)))
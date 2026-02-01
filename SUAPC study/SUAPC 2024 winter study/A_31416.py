import sys
input= sys.stdin.readline

N= int(input())
rst= []
for i in range(N):
    ta, tb, na, nb= map(int, input().split())
    """b_time= nb*tb
    a_cnt_before= b_time//ta+1
    b_time= a_cnt_before*ta
    na-= a_cnt_before
    if na>0:
        a_time_after= (na)//2*ta
    else:
        a_time_after= 0"""
    """b_time= tb*nb
    if b_time<=ta:
        a_time= (na - b_time//ta) // 2 * ta
        if a_time<0:
            a_time= 0 
        time = b_time + a_time
    else:"""

    b_time= tb*nb
    a_cnt_before= b_time//ta +1
    remain_a= na-a_cnt_before

    if remain_a>=0:
        a_time= (remain_a+1)//2*ta
        if remain_a%2:
            time= b_time + a_time
        else:
            time= a_cnt_before*ta + a_time
    else:
        time= b_time

    rst.append(time)

print('\n'.join(map(str, rst)))
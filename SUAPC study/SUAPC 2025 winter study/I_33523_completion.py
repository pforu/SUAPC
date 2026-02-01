import sys 
input = sys.stdin.readline 

#worker = boss + employee
worker_num= int(input())
checked_employee_list= [0]*(worker_num+1) #출석 부하 체크하고 돌아가지 않음  #둘째 쿼리 


def update(idx):
    while idx <= worker_num:
        checked_employee_list[idx] += 1
        idx += (idx & -idx)

def prefix_sum(idx):
    rst=0
    while idx > 0:
        rst += checked_employee_list[idx]
        idx -= (idx & -idx)
    return rst

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)


boss= [0] + list(map(int, input().split()))
days= int(input())

meeting_worker_point= []
relation_boss_employee_list= []

for i in range(days):
    meeting_worker_point.append(tuple(list(map(int, input().split()))+[i])) #L~R  ##for문의 기준 
for i in range(worker_num):
    relation_boss_employee_list.append((boss[i], i+1)) #상사, 부하 관계쌍  ##첫째 쿼리 

meeting_worker_point.sort(key= lambda x: x[0], reverse=True) #L이 큰 것부터
relation_boss_employee_list.sort(key= lambda x: x[0], reverse=True) #상사 번호가 큰 것부터 

checking_worker_cnt=0

meeting_num= [0]*days
for L, R, idx in meeting_worker_point:

    while checking_worker_cnt < worker_num and relation_boss_employee_list[checking_worker_cnt][0] >=L:
        #전체 직원 수보다 탐색한 직원 수가 적고, 탐색한 번째의 상사가 출석 
        update(relation_boss_employee_list[checking_worker_cnt][1])
        #그 부하는 체크 
        checking_worker_cnt+=1
    meeting_num[idx]= R-L+1 - interval_sum(L, R)


print('\n'.join(map(str, meeting_num))) 
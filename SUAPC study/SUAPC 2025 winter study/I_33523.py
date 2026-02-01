'''
input()
edge= [0, 0] + list(map(int, input().split()))
days= int(input())
worker_range=[]
for i in range(days):
    worker= list(map(int, input().split()))
    worker_range.append(worker)
#print(worker_range)
#print(edge)

for i in range(days):
    cnt=0
    workers= list(range(worker_range[i][0], worker_range[i][1]+1))
    #print(workers)
    for worker in workers:
        #print(worker, edge[worker])
        if edge[worker] not in workers:
            #print("****", worker)
            cnt+=1
    print(cnt)
'''

'''
# 직원 수, 직속 상사 배열 (예시)
N = 5
P = [0, 0, 1, 2, 3, 4]  # 1번 직원은 상사 없음(0), 2번 상사=1, 3번 상사=2 등

# 쿼리 리스트 (L, R, 쿼리번호)
queries = [(1, 3, 0), (2, 5, 1), (3, 5, 2)]

# 1) 직원 이벤트: (상사 번호, 직원 번호) 쌍 만들기
events = [(P[i], i) for i in range(2, N+1)]

# 2) 쿼리와 이벤트를 내림차순 정렬
queries.sort(key=lambda x: x[0], reverse=True)
events.sort(key=lambda x: x[0], reverse=True)

# 3) BIT 대신 간단한 리스트로 체크 (직원 번호 포함 여부)
checked = [False] * (N + 1)

ev = 0
results = [0] * len(queries)

for L, R, idx in queries:
    # L 이상인 상사를 가진 직원들을 체크한다
    while ev < len(events) and events[ev][0] >= L:
        checked[events[ev][1]] = True
        ev += 1

    # 쿼리 구간에서 체크된 직원 수 세기
    count_in_range = 0
    for worker in range(L, R + 1):
        if checked[worker]:
            count_in_range += 1

    # 답은 구간 크기 - 체크된 직원 수
    results[idx] = (R - L + 1) - count_in_range

# 출력
for res in results:
    print(res)
'''



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

##print(relation_boss_employee_list)
##print(meeting_worker_point)

meeting_num= [0]*days
for L, R, idx in meeting_worker_point:

    while checking_worker_cnt < worker_num and relation_boss_employee_list[checking_worker_cnt][0] >=L:
        #전체 직원 수보다 탐색한 직원 수가 적고, 탐색한 번째의 상사가 출석 
        ##print(relation_boss_employee_list[checking_worker_cnt][1])
        '''checked_employee_list[relation_boss_employee_list[checking_worker_cnt][1]]= 1'''
        update(relation_boss_employee_list[checking_worker_cnt][1])
        #print(f"idx: {relation_boss_employee_list[checking_worker_cnt][1]}")
        #그 부하는 체크 
        checking_worker_cnt+=1
        ##print(f"{idx+1}번째 날, 전체{checking_worker_cnt+1}번째 쌍, {relation_boss_employee_list[checking_worker_cnt][1]}번째 직원 체크/상사출석/미소집")
        ##print(checked_employee_list)
        ##print()
    '''worker_with_boss_num=0
    for i in range(L, R+1):
        if checked_employee_list[i]==1:
            worker_with_boss_num+=1

    meeting_num[idx]= R-L+1 - worker_with_boss_num'''
    meeting_num[idx]= R-L+1 - interval_sum(L, R)

for rst in meeting_num:
    print(rst)
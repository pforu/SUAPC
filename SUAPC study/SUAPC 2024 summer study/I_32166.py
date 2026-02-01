import sys
from math import sqrt, pow 
input = sys.stdin.readline

point_info=[] #[x, y, v] *3
line_info=[] #차선수 *3

for i in range(3):
    point_info.append(list(map(int, input().split())))

line_info.extend(list(map(int, input().split())))

road_info=[] #경로길이 *3

for i in range(3):
    if i<2:
        road_info.append(sqrt(pow(point_info[i][0]-point_info[i+1][0], 2) + pow(point_info[i][1]-point_info[i+1][1], 2)))
    else:
        road_info.append(sqrt(pow(point_info[i][0]-point_info[i-2][0], 2) + pow(point_info[i][1]-point_info[i-2][1], 2)))

#v1*t-v2*t=거리차
#그런데 그렇게 도출된 t에 대해 더 뒤에 있는 차에 대한 v*t가 지나는 경로상에 차선이 1개인 게 있으면 만나는 지점부터 
#(도출된 t), 더 속력이 낮은(앞에 있는 차에 대한 v) 차랑 같이 감 until 다음 점(경로의 끝포인트)
#그 이후로는 걍 남은 거리 가면 됨, 각각의 t를 구하면 됨 

car_info=[] #[속력, 점] *2
for i in range(3):
    if point_info[i][2]!=0:
        car_info.append([point_info[i][2], i])

car_info.sort(key=lambda x:x[0], reverse=True) #[빠른차속력, 출발점], [느린차속력, 출발점]

#두 차 변수 정리
car_speed_fast= float(car_info[0][0])
car_point_fast= car_info[0][1]
car_speed_slow= float(car_info[1][0])
car_point_slow= car_info[1][1]

#만나기 전까지의 시간, 공통 
if car_point_fast==2:
    if car_point_slow==0:
        first_distance= road_info[2]
    else:
        first_distance= road_info[2]+road_info[0]
elif car_point_fast==0:
    if car_point_slow==1:
        first_distance= road_info[0]
    else:
        first_distance= road_info[0]+road_info[1]
else:
    if car_point_slow==2:
        first_distance= road_info[1]
    else:
        first_distance= road_info[1]+road_info[2]

time_before= (first_distance) / (car_speed_fast - car_speed_slow)

total_distance_fast= car_speed_fast*time_before #만나기 전까지 빠른차가 간 거리 
total_distance_slow= car_speed_slow*time_before

total_road= sum(road_info)
#one_line= 1 in line_info #1차선 있는지 <<<<< 1차선이 그 구간인지도 판단 필요 

#print("prob", car_speed_fast, time_before)

point= car_point_fast #출발점
after_point_distance= total_distance_fast
#print(point)
#print(total_distance, road_info[point])
while True:
    if after_point_distance >= road_info[point]: #출발점에서 다음점까지보다 더 갔으면 
        after_point_distance -= road_info[point]
        point= point+1 if point<2 else point-2
    else:
        break

#print(total_distance)


if total_distance_fast >= total_road or line_info[point]!=1:
    #case1: 속도차로 아예 안 만남 
    #case2: 만나지만 해당 구간이 1차선이 아님 
    time_total_fast= total_road / car_speed_fast
    time_total_slow= total_road / car_speed_slow

else:
    #case3: 만나고 해당 구간이 1차선임 
    #현재 point: 만난 구간
    #현재 total_distance: 해당 구간에서 얼마나 갔는지 
    time_meet= (road_info[point] - after_point_distance) / car_speed_slow
    #print("time meet", time_meet)

    total_distance_fast+= time_meet*car_speed_slow
    total_distance_slow+= time_meet*car_speed_slow

    #print("total distance after meet", total_distance_fast, total_distance_slow)
    
    time_after_fast= (total_road - total_distance_fast) / car_speed_fast
    time_after_slow= (total_road - total_distance_slow) / car_speed_slow

    time_total_fast= time_before + time_meet + time_after_fast
    time_total_slow= time_before + time_meet + time_after_slow

    #print()
    #print(time_before, time_meet, time_after_fast, time_after_slow)

time_total= [0]*3
time_total[car_point_fast]= time_total_fast
time_total[car_point_slow]= time_total_slow
for i in range(3):
    if time_total[i]==0:
        time_total[i]= '-'

print('\n'.join(map(str, time_total)))

# 3 4 6.5 12
# timebefore=3, timemeet=1, timeafterfast=2.5, timeafterslow=8
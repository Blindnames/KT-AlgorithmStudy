## 모험가 길드 
# 조건 1. 첫째줄에 모험가의 수 N이 주어집니다. (1<=N<=100,000)
# 조건 2. 둘째줄에 모험가의 공포도의 값을 N이하의 자연수로 지어지며, 각 자연수는 공백으로 구분합니다.

# 출력 조건 : 여행을 떠날수 있는 그룹 수의 최댓값을 출력합니다.

n = int(input("모험가의 수를 입력해주세요"))  # 모험가의 수
scr = list(map(int, input('공포도 값을 입력해주세요').split())) #공포도 값을 리스트 형태로 입력

scr.sort() # 공포도를 오름차순 정렬.

grp = 0 # 총 그룹의 수
add= 0 # 추가된 그룹의 수

for i in scr :
    add += 1 # 추가된 그룹수 +1
    if add >= i :
        grp +=1
        add = 0
print(add)
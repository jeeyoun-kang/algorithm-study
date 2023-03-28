import sys
input = sys.stdin.readline

n = int(input()) # 계란의 수
egg = [list(map(int, input().split())) for _ in range(n)] #계란의 내구도와 무게를 저장하는 리스트


def solution(now):
    if now == len(egg): # 가장 오른쪽에 위치한 계란일 때
        cnt=0
        for s,w in egg:
            if s<=0:
                cnt+=1
        return cnt

    if egg[now][0]<=0: # 지금 손에 든 계란이 깨졌을 때
        return solution(now+1)

    for j in range(len(egg)): # 깨지지 않은 계란이 남아있는지 확인
        if j == now:
            continue
        if egg[j][0]>0:
            break
    else: # 깨지지 않은 계란이 없을때
        return solution(now+1)

    # 칠 수 있는 계란을 깨보는 과정
    answer=0
    for k in range(len(egg)):
        if k==now:
            continue
        if egg[k][0]<=0:
            continue

        egg[k][0] -=egg[now][1]
        egg[now][0] -= egg[k][1]

        answer = max(answer,solution(now+1))

        # 하나의 계란을 친 후 다시 더해서 원래 상태로 만들어주고 다음 계란 치기
        egg[k][0]+=egg[now][1]
        egg[now][0]+=egg[k][1]
    return answer

print(solution(0))
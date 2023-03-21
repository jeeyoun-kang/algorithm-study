import sys
input = sys.stdin .readline
n,m = map(int, input().split()) #나무의 수와 가져가려는 나무의 길이

trees = list(map(int, input().split()))

left, right = 0, max(trees) #시작점과 끝점을 정함

while left <= right:
    mid = (left + right) // 2
    total = 0

    for tree in trees:
        if tree >= mid:
            total += tree - mid

    if total >= m: #가져가려는 나무가 m보다 클때
        left = mid + 1
    else:
        right = mid - 1

print(right)
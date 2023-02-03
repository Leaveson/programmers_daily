from heapq import *
#Programmers
#LEVEL 2
# 뒤에 있는 큰 수 찾기
#문제풀이시간 (30분 but 시간초과연속 나옴으로 인한 해설확인)
# heapq 이용
def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    h = []
    for i, val in enumerate(numbers):
        while h and h[0][0] < val:
            _, idx = heappop(h)
            answer[idx] = val
        heappush(h, (val, i))
    return answer

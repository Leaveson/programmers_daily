#Programmers
#LEVEL 2
#시소 짝궁
#문제풀이시간 (10분 but 원래 풀이였던 모든 combinations을 비교하는건 시간초과가 나서 counter class를 통한 같은 object를 우선적으로 세고 보다 효율적으로 계산)
# counter 이용
from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    for k,v in count.items():
        if v > 1:
            answer += v * (v-1) / 2
    for weight in count.keys():
        for a in [1/2, 2/3, 3/4]:
            if weight * a in count.keys():
                answer += count[weight * a] * count[weight]
    return answer

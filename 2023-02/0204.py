#Programmers
#LEVEL 2
#숫자변환하기
#문제풀이시간 (1시간 and 원래 풀이였던 숫자를 키워가기를 시도하면 시간초과가 나서 나눗셈을 통한 풀이로 변경)
# stack 이용
from collections import deque
def solution(x, y, n):
    queue = deque()
    count = 0
    queue.append((y,count))
    while(queue):
        y, count = queue.popleft()
        if x == y:
            return count
        if x > y:
            continue
        if y % 3 == 0:
            queue.append((y//3, count+1))
        if y % 2 == 0:
            queue.append((y // 2, count+1))
        if n + x <= y:
            queue.append((y-n, count + 1))
    answer = -1
    return answer

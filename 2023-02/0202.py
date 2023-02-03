#Programmers
#LEVEL 2
# 무인도 여행
#문제풀이시간 (1시간 초과 및 해설확인)
# stack 이용
from collections import deque
def solution(maps):
    M = len(maps)
    N = len(maps[0])
    
    answer = []
    visited = [[0 for j in range(N)] for i in range(M)]
    for row in range(M):
        for col in range(N): 
            if (maps[row][col] == "X") or (visited[row][col] == 1):
                continue
            queue = deque()            
            queue.append((row, col))
            visited[row][col] = 1
            food = int(maps[row][col])
            while(queue):
                row1, col1 = queue.popleft()
                for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_col = col1 + x
                    new_row = row1 + y
                    if 0<=new_row<M and 0<=new_col<N and visited[new_row][new_col]==0 and maps[new_row][new_col]!='X':
                        queue.append((new_row, new_col))
                        visited[new_row][new_col] = 1
                        food += int(maps[new_row][new_col])
            answer.append(food)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer

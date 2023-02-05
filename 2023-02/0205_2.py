#Programmers
#LEVEL 2
#호텔 대실
#문제풀이시간 (30분)

from collections import deque

def solution(book_time):
    answer = 0
    queue = deque()
    conv_book_time = []
    for start, end in book_time:
        start_lst = list(map(int, start.split(":")))
        end_lst = list(map(int, end.split(":")))
        conv_book_time.append((start_lst[0]*100+start_lst[1], end_lst[0]*100+end_lst[1]))
    conv_book_time = sorted(conv_book_time, key=lambda x:(x[0],x[1]))
    for start, end in conv_book_time:
        i = 0
        iter = len(queue)
        find = False
        while(i < iter):
            using_st, using_et = queue.popleft()
            ready_time = using_et + 10
            if ready_time % 100 >= 60:
                ready_time += (100 - 60)
            if ready_time <= start:
                queue.append((start, end))
                find = True
                break
            else:
                 queue.append((using_st, using_et))
            i += 1
        if not find:
            queue.append((start, end))
        # queue = deque(sorted(queue, key=lambda x:(x[0],x[1]))) -> 이게 필요할까?
    answer = len(queue)
    return answer

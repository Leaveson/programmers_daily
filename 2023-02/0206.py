#Programmers
#LEVEL 2
#택배 배달과 수거하기
#문제풀이시간 (25분)

from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = -1
    d_queue = deque(deliveries)
    p_queue = deque(pickups)
    length = 0
    
    while(d_queue or p_queue):
        while(d_queue):
            if d_queue[-1] == 0:
                d_queue.pop()
            else:
                break
        while(p_queue):
            if p_queue[-1] == 0:
                p_queue.pop()
            else:
                break
        length += 2 * max(len(d_queue), len(p_queue))
        total_dnum = 0 
        total_pnum = 0
        while(d_queue):
            d_num = d_queue.pop()
            total_dnum += d_num
            if total_dnum > cap:
                d_num = (total_dnum - cap)
                d_queue.append(d_num)
                break
        while(p_queue):
            p_num = p_queue.pop()
            total_pnum += p_num
            if total_pnum > cap:
                p_num = (total_pnum - cap)
                p_queue.append(p_num)
                break
    answer = length   
    return answer

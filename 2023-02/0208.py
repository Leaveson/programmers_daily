#Programmers
#LEVEL 2
#마법의 엘리베이터
#문제풀이시간 (40분)
def solution(storey):
    answer = 0
    while(storey!=0):
        n = storey % 10 
        if n > 5:
            answer += (10 - n)
            storey += (10 - n)
        elif n == 5 and (storey // 10) % 10 >= 5:
                answer += 5
                storey += 5
        else:
            answer += n
        storey = storey // 10
    return answer

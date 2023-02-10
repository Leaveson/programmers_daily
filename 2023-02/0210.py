#Programmers
#LEVEL 2
#해시테이블
#문제풀이시간 (10분)
def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        s = 0
        for element in data[i-1]:
            s += element % i 
        if i == row_begin:
            answer = s
        else:
            answer = answer ^ s
    return answer

#Programmers
#LEVEL 2
#요격시스템
#문제풀이시간 (20분)
# Sorting문제

def solution(targets):
    answer = 0
    sorted_target = sorted(targets, key=lambda x: x[0])
    for i, arr in enumerate(sorted_target):
        if i == 0:
            s = arr[0]
            e = arr[1]
        else:
            if arr[0] < high_num:
                s = arr[0]
                if arr[1] < high_num:
                    e = arr[1]
                continue
            else:
                answer += 1
                s = arr[0]
                e = arr[1]
    answer += 1
    return answer

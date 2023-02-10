#Programmers
#LEVEL 2
#유사 칸토어 비트열
#문제풀이시간 (2시간)
def cal_one_count(pos):
    result = 0
    pow = 0
    one_num_lst = [0, 1, 2, 2, 3]
    new_num = ""
    while(pos !=0):
        rest = pos % 5
        new_num = str(rest) + new_num
        pos = pos // 5
    for i, digit in enumerate(new_num):
        if int(digit) == 2:
            result += 4 **(len(new_num) - 1 - i) * one_num_lst[int(digit)]
            break
        else:
            result += 4 **(len(new_num) - 1 - i) * one_num_lst[int(digit)]
    return result
        
def solution(n, l, r):
    return cal_one_count(r) - cal_one_count(l-1)

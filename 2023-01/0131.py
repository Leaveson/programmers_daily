#Programmers
#LEVEL 1
# 다트게임
#문제풀이시간 (40분)
from collections import defaultdict
def cal_power(num, alpha):
    if alpha == "S":
        return num
    elif alpha == "D":
        return num**2
    else:
        return num**3
def solution(dartResult):
    answer = 0
    is_ten = False
    score = []
    power = []
    effect = defaultdict(str)
    round_per_score = []
    for i, word in enumerate(dartResult):
        if word.isdigit():
            if is_ten:
                is_ten=False
                continue
            if dartResult[i+1].isdigit():
                score.append(10)
                is_ten = True
            else:
                score.append(int(word))
        elif word.isalpha():
            power.append(word)
        else:
            effect[str(len(power))] = word
    for i in range(3):
        if i == 0 and (effect[str(i+1)] == "*"):
            round_per_score.append(2 * cal_power(score[i], power[i]))
        elif effect[str(i+1)] == "#":
            round_per_score.append(-1 * cal_power(score[i], power[i]))
        elif (effect[str(i+1)] == "*"):
            round_per_score[i-1] = round_per_score[i-1] * 2
            round_per_score.append(cal_power(score[i], power[i])*2)
        else:
            round_per_score.append(cal_power(score[i], power[i]))
    answer = sum(round_per_score)
    return answer

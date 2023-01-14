# Programmers
# LEVEL 1
# 성격유형검사하기
# 풀이 시작시간 10:05AM - 10:30AM

def compare_type(score, personal1, personal2):
    if score[personal1] > score[personal2]:
        return personal1
    elif score[personal1] < score[personal2]:
        return personal2
    else:
        if personal1 < personal2:
            return personal1
        else:
            return personal2

def solution(survey, choices):
    score = {"R" : 0, "T": 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    personal_types = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    choice_score = [3, 2, 1, 0, 1, 2, 3]
    for i, typ in enumerate(survey):
        for personal_type in personal_types:
            if typ == personal_type:
                if choices[i] == 4:
                    break
                elif choices[i] < 4:
                    score[typ[0]] += choice_score[choices[i]-1]
                    break
                else:
                    score[typ[1]] += choice_score[choices[i]-1]
                    break
    a = compare_type(score, "R", "T")
    b = compare_type(score, "C", "F")
    c = compare_type(score, "J", "M")
    d = compare_type(score, "A", "N")
    
        
    answer = a+b+c+d
    return answer

if __name__ == "__main__":
    testcases = [[["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]],[["TR", "RT", "TR"], [7, 1, 3]]]
    answer = ["TCMA","RCJA"]
    for i, testcase in enumerate(testcases):
        if answer[i] == solution(*testcase):
            print("success")
        else:
            print("fail")

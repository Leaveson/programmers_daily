#Programmers
#LEVEL 1
# 실패율
#문제풀이시간 (30분)

from collections import defaultdict

def solution(N, stages):
    answer = []
    stage_per_num = defaultdict(int)
    failure_per_stage = {} 
    state_culsum = 0
    for stage in stages:
        stage_per_num[str(stage)] += 1
    for i in range(N):
        if stage_per_num[str(i+1)] == 0:
            failure_per_stage[str(i+1)] = 0
        else:
            failure_per_stage[str(i+1)] = stage_per_num[str(i+1)] / (len(stages) - state_culsum)
            state_culsum += stage_per_num[str(i+1)]
    failure_per_stage = sorted(failure_per_stage.items(), key = lambda x : x[1], reverse=True)
    for key, val in failure_per_stage:
        answer.append(int(key))
    return answer
  
if __name__ == "__main__":
    testcases = [[5, [2, 1, 2, 6, 2, 4, 3, 3]],[4, [4,4,4,4,4]]]
    answers = [[3,4,2,1,5], [4,1,2,3]]
    for answer, testcase in zip(answers, testcases):
        if answer == solution(*testcase):
            print("success")
        else:
            print("fail")

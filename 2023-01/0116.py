#Programmers
#LEVEL1
#신고결과 받기
#문제 풀이시간 9:50PM - 10:25PM(25min)

from collections import defaultdict

def solution(id_list, report, k):
    # answer = []
    id_score_dict = {user_id : defaultdict(int) for user_id in id_list}
    reported_score = {user_id : 0 for user_id in id_list}
    message_count = {user_id : 0 for user_id in id_list}
    reported_to_report = defaultdict(set)
    
    for alarm in report:
        user_id, reported_id = alarm.split(' ')
        id_score_dict[user_id][reported_id] += 1

        reported_to_report[reported_id].add(user_id)
    
        if id_score_dict[user_id][reported_id] >=2:
            continue
        else:
            reported_score[reported_id] += 1

    for key, value in reported_score.items():
        if value >= k:
            for user_id in reported_to_report[key]:
                message_count[user_id] += 1
    answer = [answer for answer in message_count.values()]
    return answer

if __name__ == "__main__":
    testcases = [[["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2],[["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3]]
    answer = [[2,1,1,0], [0,0]]
    for i, testcase in enumerate(testcases):
        if answer[i] == solution(*testcase):
            print("success")
        else:
            print("fail")

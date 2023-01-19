#Programmers
#LEVEL 1
#키패드 누르기
#문제풀이시간 10:20PM - 10:46PM(26분)

from collections import defaultdict
def solution(numbers, hand):
    answer = ""
    distance = defaultdict(dict)
    left_hand = ["*", "7", "4", "1"]
    distance["*"] = {"2":4, "5":3, "8":2, "0":1}
    distance["7"] = {"2":3, "5":2, "8":1, "0":2}
    distance["4"] = {"2":2, "5":1, "8":2, "0":3}
    distance["1"] = {"2":1, "5":2, "8":3, "0":4}
    
    right_hand = ["#", "9", "6", "3"]
    
    distance["#"] = {"2":4, "5":3, "8":2, "0":1}
    distance["9"] = {"2":3, "5":2, "8":1, "0":2}
    distance["6"] = {"2":2, "5":1, "8":2, "0":3}
    distance["3"] = {"2":1, "5":2, "8":3, "0":4}
    
    distance["2"] = {"2":0, "5":1, "8":2, "0":3}
    distance["5"] = {"2":1, "5":0, "8":1, "0":2}
    distance["8"] = {"2":2, "5":1, "8":0, "0":1}
    distance["0"] = {"2":3, "5":2, "8":1, "0":0}
    lh_pos = "*"
    rh_pos = "#"
    
    for number in numbers:   
        
        number = str(number)
        if number in left_hand:
            answer += "L"
            lh_pos = number
        elif number in right_hand:
            answer += "R"
            rh_pos = number
        else:
            print(number)
            l_distance = distance[lh_pos][number]
            r_distance = distance[rh_pos][number]
            if l_distance < r_distance:
                lh_pos = number
                answer += "L"
            elif l_distance > r_distance:
                rh_pos = number
                answer += "R"
            else:
                if hand == "left":
                    lh_pos = number
                    answer += "L"
                else:
                    rh_pos = number
                    answer += "R"
    return answer

if __name__ == "__main__":
    testcases = [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"]]
    answer = ["LRLLLRLLRRL"]
    for i, testcase in enumerate(testcases):
        if answer[i] == solution(*testcase):
            print("success")
        else:
            print("fail")

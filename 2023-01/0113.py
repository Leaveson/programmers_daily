#Programmers
#LEVEL 1
# 옹알이(2)
#문제 풀이시간 : 11:05 AM - 11:35AM

def solution(babbling):
    answer = 0
    babble_word2 = [ "ye", "ma"]
    babble_word3 = ["aya", "woo"]
    for babble in babbling:
        pos = 0
        prev_word = None
        done = False
        while(not done):
            if babble[pos:pos+2] in babble_word2:
                if prev_word != babble[pos:pos+2]:
                    if pos + 2 == len(babble):
                        done = True
                        answer += 1
                    prev_word = babble[pos:pos+2]
                    pos = pos + 2
                else:
                    done = True
            elif babble[pos:pos+3] in babble_word3:
                if prev_word != babble[pos:pos+3]:
                    if pos + 3 == len(babble):
                        done = True
                        answer += 1
                    prev_word = babble[pos:pos+3]
                    pos = pos + 3
                else:
                    done = True  
            else:
                done = True
    return answer
 
if __name__ == "__main__":
    testcases = [["aya", "yee", "u"], ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]]
    answer = [1,2]
    for i, testcase in enumerate(testcases):
        if answer[i]==solution(testcase):
            print("success")
        else:
            print("fail")

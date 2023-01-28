#Programmers
#LEVEL 1
# 크레인 인형뽑기 게임
#문제풀이시간 (2시간 30분)

def solution(board, moves):
    blanket = []
    answer = 0
    for move in moves:
        element1 = 0
        pos = 0
        while pos !=  len(board) and (element1) == 0:
            element1 = board[pos][move - 1]
            if element1 != 0:
                board[pos][move-1] = 0
            pos += 1  
        if element1 == 0:
            continue
        if len(blanket) == 0:
            blanket.append(element1)
        else:
            element2 = blanket.pop()
            if element1 == element2:
                answer += 2
            else:
                blanket.append(element2)
                blanket.append(element1)
    return answer

if __name__ == "__main__":
    testcases = [[[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]]]
    answers = [4]
    for answer, testcase in zip(answers, testcases):
        if answer == solution(*testcase):
            print("success")
        else:
            print("fail")

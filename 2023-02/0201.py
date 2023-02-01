#Programmers
#LEVEL 1
#비밀지도
#문제풀이시간 09:00 - 09:15 (15분)
def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for element in arr1:
        code = ""
        for i in range(n, 0, -1):
            code += str(element//(2**(i-1)))
            element = element % (2**(i-1))
        map1.append(code)
    for element in arr2:
        code = ""
        for i in range(n, 0, -1):
            code += str(element//(2**(i-1)))
            element = element % (2**(i-1))
        map2.append(code)
    for a1, a2 in zip(map1, map2):
        code = ""
        for i in range(n):
            if a1[i] == "1" or a2[i] == "1":
                code += "#"
            else:
                code += " "
        answer.append(code)
    return answer

# Programmers
# LEVEL 1
# 숫자 문자열과 영단어
# 문제 풀이 시작 9:20AM - 9:39AM (19분)

def solution(s):
    string_to_num = {"zero" : "0", "one" : "1", "two":"2", "three":"3", "four":"4", "five":"5",
                    "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    # num = ["0", "1", "2", "3", "4", "5", ]
    answer = ""
    len_alpha_num = 0
    pos = 0
    while(pos < len(s)):
        if s[pos].isalpha():
            if s[pos] == "z":
                pos += 4
                answer += string_to_num["zero"]
            elif s[pos] == "o":
                pos += 3
                answer += string_to_num["one"]
            elif s[pos] == "t":
                if s[pos+2] == "o":
                    pos += 3
                    answer += string_to_num["two"]
                else:
                    pos += 5
                    answer += string_to_num["three"]
            elif s[pos] == "f":
                if s[pos+3] == "r":
                    pos += 4
                    answer += string_to_num["four"]
                else:
                    pos += 4
                    answer += string_to_num["five"]
            elif s[pos] == "s":
                if s[pos+2] == "x":
                    pos += 3
                    answer += string_to_num["six"]
                else:
                    pos += 5
                    answer += string_to_num["seven"]
            elif s[pos] == "e":
                pos += 5
                answer += string_to_num["eight"]
            elif s[pos] == "n":
                pos += 4
                answer += string_to_num["nine"]
        else:
            answer += s[pos]
            pos += 1
    answer = int(answer)
    return answer

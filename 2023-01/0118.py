#programmers
#LEVEL1
#신규아이디추천
#문제 풀이시간 9:20AM - 9:50AM(30분)

import re

def solution(new_id):
    new_id = new_id.lower()
    id_removed_special_mark = ""
    for i, word in enumerate(new_id):
        if word.isalpha() or word.isdigit() or word == "-" or  word =="." or word =="_":
            id_removed_special_mark += word
    
    id_removed_special_mark = re.sub(r"[.]+", ".", id_removed_special_mark)
    id_removed_special_mark= id_removed_special_mark.strip(".")
    if id_removed_special_mark == "":
        id_removed_special_mark += "a"
    if len(id_removed_special_mark) >= 16:
        id_removed_special_mark = id_removed_special_mark[:15]
        if id_removed_special_mark[-1] == ".":
            id_removed_special_mark = id_removed_special_mark[:-1]
    if len(id_removed_special_mark) <= 2:
        while(len(id_removed_special_mark)<=2):
            id_removed_special_mark += id_removed_special_mark[-1]
    answer = id_removed_special_mark
    return answer

if __name__ == "__main__":
    testcases = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    answer = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]
    for i, testcase in enumerate(testcases):
        if answer[i] == solution(testcase):
            print("success")
        else:
            print("fail")

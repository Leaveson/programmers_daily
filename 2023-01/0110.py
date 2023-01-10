def solution(s):
    length = len(s)
    pos = 0
    prev_pos = 0
    x = None
    same = 0
    diff = 0
    split_letter = []
    first = True
    while(pos < length):     
        if first:
            x = s[pos]
            first = False
            same +=1
            if pos == length - 1:
                split_letter.append(s[prev_pos:])
            pos += 1
        else:
            if pos == length - 1:
                split_letter.append(s[prev_pos:])
            else:
                if s[pos] == x:
                    same += 1
                else:
                    diff += 1
                if same == diff:
                    split_letter.append(s[prev_pos:pos+1])
                    prev_pos = pos + 1
                    same = 0
                    diff = 0
                    first = True
            pos += 1
         
    answer = len(split_letter)
    return answer


if __name__ == "__main__":
    testcases = ["banana", "abracadabra", "aaabbaccccabba"]
    answer = [3, 6, 3]
    for i, testcase in enumerate(testcases):
        if answer[i] == solution(testcase):
            print("success")
        else:
            print("fail")

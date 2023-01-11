#걸린시간 1hour 15min
def solution(number, limit, power):
    count = []
    for i in range(number):
        num = 0
        for j in range(int((i+1)**(1/2))):
            if ((i + 1) % (j + 1) == 0):
                if (i + 1) // (j + 1) == j+1:
                    num += 1
                else:
                    num += 2
            if num > limit:
                count.append(power)
                break
            if j == int((i+1)**(1/2)) - 1:
                count.append(num)
                
    answer = sum(count)
    return answer
  
if __name__ == "__main__":
  testcases = [[5,3,2], [10, 3, 2]]
  answer = [10,21]
  for i, testcase in enumerate(testcases):
      if answer[i] == solution(*testcase):
          print("success")
      else:
          print("fail")

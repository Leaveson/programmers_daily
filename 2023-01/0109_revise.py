def day2num(yy, mm, dd):
    return (yy - 2000) * 28 * 12 + mm * 28 + dd
def solution(today, terms, privacies):
    answer = []
    duration = {}
    yy, mm, dd = list(map(int, today.split('.')))
    todaynum = day2num(yy, mm, dd)
    for term in terms:
        key, val = term.split(' ')
        duration[key] = val
    for i, privacy in enumerate(privacies):
        start_day, dur_type = privacy.split(' ')
        yy, mm, dd = list(map(int, start_day.split('.')))
        start_daynum = day2num(yy, mm, dd)
        print(start_daynum)
        print(todaynum)
        if todaynum - start_daynum >= int(duration[dur_type]) * 28:    
            answer.append(i+1)
    print(answer)
    return answer
  
if __name__ == "__main__":
  test_cases = []
  test_cases.append(["2022.05.19", ["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]])
  test_cases.append(["2020.01.01", ["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]])

  answers = [[1,3], [1, 4, 5]]

  for test_case, answer in zip(test_cases, answers):
      my_sol = solution(*test_case)
      if my_sol == answer:
          print("sucess")
      else:
          print("fail")

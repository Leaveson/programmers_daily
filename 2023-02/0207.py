#Programmers
#LEVEL 2
#이모티콘 할인행사
#문제풀이시간 (45분)
from itertools import product
def solution(users, emoticons):
    answer = []
    all_case = []
    sale_ratio = [10, 20, 30, 40]
    permu = product(sale_ratio, repeat=len(emoticons))
    for per in permu:
        member_num = 0
        mem_price = 0
        for sale, price in users:       
            total_price = 0
            for emoticon, ratio in zip(emoticons, per):
                if (ratio) >= sale:
                    total_price += (100-ratio)/100 * emoticon
            if total_price >= price:
                member_num += 1
            else:
                mem_price += total_price
        all_case.append([member_num, mem_price])       
    all_case = sorted(all_case, key=lambda x: (-x[0], -x[1]))
    answer = all_case[0]
    return answer

# 1hours 32min
from collections import deque

def solution(ingredient):
    answer = 0
    store_ingredient = deque()
    make_hamberger = False
    for ingred in ingredient:
        store_ingredient.append(ingred)
        if len(store_ingredient) >= 4 :
            a = store_ingredient.pop()
            b = store_ingredient.pop()
            c = store_ingredient.pop()
            d = store_ingredient.pop()
            
            store_ingredient.append(d)
            store_ingredient.append(c)
            store_ingredient.append(b)
            store_ingredient.append(a)
            if [d, c, b, a] == [1, 2, 3, 1]:
                make_hamberger = True
                answer += 1
        if make_hamberger:
            for i in range(4):
                store_ingredient.pop()
            make_hamberger = False
            
    return answer

if __name__ == "__main__":
    testcases = [[2, 1, 1, 2, 3, 1, 2, 3, 1], [1, 3, 2, 1, 2, 1, 3, 1, 2],[1, 1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1],[1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 3, 3, 3, 2, 1, 2, 3, 1] ]
    answer = [2, 0, 3, 5]
    for i, testcase in enumerate(testcases):
        if answer[i]==solution(testcase):
            print("success")
        else:
            print("fail")

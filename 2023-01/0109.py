#풀이 시간 시작 : 10:50AM
# 풀이 총 걸린시간 1hours
def solution(today, terms, privacies):
    answer = []
    val_types = {}
    yy, mm, dd = today.split('.')
    
    yy = int(yy)
    mm = int(mm)
    dd = int(dd)
    
    for term in terms:
        validity = term.split(' ')
        val_types[validity[0]] = int(validity[1])
    for i, privacy in enumerate(privacies):
        start_day, val_type  = privacy.split(' ')
        S_yy, S_mm, S_dd = start_day.split('.')
        
        S_yy = int(S_yy)
        S_mm = int(S_mm)
        S_dd = int(S_dd)
        
        val = val_types[val_type]
        plus_y = val // 12
        plus_m = val % 12    
        S_yy += plus_y
        S_mm += plus_m
        S_dd -= 1
        if S_mm > 12:
            S_yy += 1
            S_mm -= 12
        if S_dd == 0:
            S_mm -=1
            S_dd = 28
        if S_yy < yy:
            answer.append(i+1)
        elif (S_yy == yy) and (S_mm < mm):
            answer.append(i+1)
        elif (S_yy == yy) and (S_mm ==  mm) and (S_dd < dd):
            answer.append(i+1)
            
    return answer

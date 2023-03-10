# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    X,Y=str(X),str(Y)
    xandy=list(set(X)&set(Y))
    if not xandy:
        return '-1'
    elif xandy == ['0']:
        return '0'
    xandy.sort(reverse=True)
    xydic={}
    answer=[]
    for xy in xandy:
        xydic[xy]=min(X.count(xy),Y.count(xy))
    for k,v in xydic.items():
        answer.append(k*v)
    return ''.join(answer)

# 테스트 11 〉	통과 (166.20ms, 29.9MB)
# 테스트 12 〉	통과 (178.49ms, 30.1MB)
# 테스트 13 〉	통과 (206.19ms, 30.1MB)
# 테스트 14 〉	통과 (166.98ms, 29.9MB)
# 테스트 15 〉	통과 (140.43ms, 29.8MB)

def solution(X, Y):
    X,Y=str(X),str(Y)
    xandy=list(set(X)&set(Y))
    if not xandy:
        return '-1'
    elif xandy == ['0']:
        return '0'
    xandy.sort(reverse=True)
    answer=[xy*min(X.count(xy),Y.count(xy)) for xy in xandy ]
    return ''.join(answer)

# 테스트 11 〉	통과 (139.16ms, 30MB)
# 테스트 12 〉	통과 (131.48ms, 29.9MB)
# 테스트 13 〉	통과 (123.17ms, 30MB)
# 테스트 14 〉	통과 (134.14ms, 30MB)
# 테스트 15 〉	통과 (130.26ms, 30.1MB)
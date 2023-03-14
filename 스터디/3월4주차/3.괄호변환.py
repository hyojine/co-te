# https://school.programmers.co.kr/learn/courses/30/lessons/60058 
# 균형잡힌 괄호 문자열: '(' 의 개수와 ')' 의 개수가 같다
# 올바른 괄호 문자열: '('와 ')'의 괄호의 짝도 모두 맞을 경우

def check(u):
    stack=[]
    for uu in u:
        if uu=='(':
            stack.append(uu)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ''
    p_open,p_close=0,0
    for i in range(len(p)):
        if p[i]=='(':
            p_open+=1
        else:
            p_close+=1
        if p_open == p_close:
            u,v= p[:i+1],p[i+1:]
            break
    if check(u):
        return u+solution(v)
    else:
        answer='('+solution(v)+')'
        for uu in u[1:len(u)-1]:
            if uu == '(':
                answer += ')'
            else:
                answer += '('
        return answer
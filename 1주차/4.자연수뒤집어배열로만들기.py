def solution(n):
    answer = ''
    string=str(n)
    for i in range(len(string)) :
        answer+=string[-(i+1)]
    answer=list(answer)
    for i in range(len(answer)):
        answer[i]=int(answer[i])    
    return answer
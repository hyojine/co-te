# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score=0
        for p in photo[i]:
            if p in name:
                score+=(yearning[name.index(p)])
        answer.append(score)       
    return answer
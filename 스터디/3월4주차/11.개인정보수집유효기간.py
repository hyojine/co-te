# https://school.programmers.co.kr/learn/courses/30/lessons/150370

# 개인정보 수집일자에 약관종류에 따른 기간을 더한 후 오늘 날짜랑 비교
# 오늘 날짜랑 년 같으면-> 월 -> 일 순으로 비교
# privacis의 날짜는 today 이전의 날짜만 주어집니다.

def solution0(today, terms, privacies):
    terms=dict([x.split(' ') for x in terms])# 약관종류,유효기간
    # print(terms) # {'A': '6', 'B': '12', 'C': '3'}
    privacies=[x.split(' ') for x in privacies]# 날짜,약관종류
    # print(privacies) # [['2021.05.02', 'A'], ['2021.07.01', 'B'], ['2022.02.19', 'C'], ['2022.02.20', 'C']]
    today=[int(x) for x in today.split('.')]# y,m,d
    # print(today) #[2022, 5, 19]
    answer = []
    for i,p in enumerate(privacies):
        date, kinds = p
        y,m,d=map(int,date.split('.'))
        d=d+int(terms[kinds])*28
        if d>28:
            if d%28 != 0:
                m+=d//28
                d=d%28
            else:
                m+=d//28-1
                d=28
        if m>12:
            if m%12 != 0:
                y+=m//12
                m=m%12
            else:
                y+=m//12-1
                m=12
        if y<today[0]:
            answer.append(i+1)
        elif y==today[0] and m<today[1]:
            answer.append(i+1)
        elif y==today[0] and m==today[1] and d<=today[2]:
            answer.append(i+1)
    return answer

# 총 일수 비교하는 방법
def solution(today, terms, privacies):
    today=list(map(int,today.split('.')))
    std=today[0]*12*28+today[1]*28+today[2]
    terms=dict([x.split(' ') for x in terms])
    privacies=[x.split(' ') for x in privacies]
    answer=[]
    for i,p in enumerate(privacies):
        date,kind = p
        date=list(map(int,date.split('.')))
        y=date[0]
        m=date[1]
        d=date[2]
        if y*12*28+m*28+d+int(terms[kind])*28<=std:
            answer.append(i+1)
    return answer

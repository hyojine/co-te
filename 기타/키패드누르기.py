# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    hand='R' if hand =='right' else 'L'
    keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    keypad_cord={}
    for i in range(len(keypad)):
        for j,val in enumerate(keypad[i]):
            keypad_cord[val]=(i,j)
    answer = ''
    l='*'
    r='#'
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            l=num
        elif num in [3,6,9]:
            answer+='R'
            r=num
        else:
            x,y=keypad_cord[num]
            xr,yr=keypad_cord[r]
            xl,yl=keypad_cord[l]
            dr=abs(x-xr)+abs(y-yr)
            dl=abs(x-xl)+abs(y-yl)
            if dr>dl:
                answer+='L'
                l=num
            elif dr==dl:
                answer+=hand
                if hand=='L':
                    l=num
                else:
                    r=num
            else:
                answer+='R'
                r=num         
    return answer
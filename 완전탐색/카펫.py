def solution(brown, yellow):
    size = brown+yellow
    w=0
    h=0

    while size!=w*h:
        h+=1
        w=int((brown+4)/2-h)
        print(w,h)
        print(type(w),type(h))
      
    return [w,h]
         
print(solution(10,2))

# sympy 모듈 사용
# from sympy import symbols, solve

# def solution(brown, yellow):
#     w, h = symbols('w','h')
#     eq1= w*h- brown*yellow
#     eq2= w+h-(brown+4)/2
#     # answer=
    # print(solve((eq1,eq2),dict=True))
    # if anwser[0]['w']<anwser[0]['h']:
    #     anwser[0]['w'],anwser[0]['h']=anwser[0]['h'],anwser[0]['w']
    # return [anwser[0]['w'],anwser[0]['h']]

# def solution(brown, yellow):
#     size = brown+yellow
#     w=0
#     h=0

#     while size!=w*h:
#         h+=1
#         w=int((brown+4)/2-h)
#         print(w,h)
#         print(type(w),type(h))
      
#     return [w,h]

# yellow의 임의의 한변의 길이를 기준으로 품
def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow%i==0 and 2*(i+2+yellow/i)==brown:
            print(yellow/i+2)
            print(type(yellow/i+2))
            return [int(yellow/i+2),i+2]
         
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

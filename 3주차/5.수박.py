def solution(n):
    s=''
    for i in range(n):
        if i%2==0:
            s+='수'
        else:
            s+='박'
    return s
print(solution(3))

def solution(n):
    return "".join(["수박"[i%2] for i in range(n)]) 
    # 2로 나누니까 어차피 나머지가 0또는 1
    # -> '수' 또는 '박'을 리스트에 담아서 공백없이 문자열로 합쳐줌
# 빵 – 야채 – 고기 - 빵 1231  정수 배열 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다
#시간초과
def solution(ingredient):
    str_ing=''.join(map(str,ingredient))
    cnt=0
    while '1231' in str_ing:
        str_ing=str_ing.replace('1231','',1)
        cnt+=1
    return cnt

# 시간초과 안나는데 어디서 틀리는 건지 모르겠음
# 앞에꺼부터 하나씩 해야되는데 한꺼번에 여러개 해서 틀리는 건가??그런거같아하하
def solution2(ingredient):
    str_ing=''.join(map(str,ingredient))
    cnt=0
    for _ in range(len(ingredient)):
        str_ing=str_ing.replace('1231','k') # 문자열에 '1231' 없는 경우에도 오류 안남
        print(str_ing)
        if d:=str_ing.count('k'):
            cnt+=d
            str_ing=str_ing.replace('k','')
        else:
            break
    return cnt

def solution3(ingredient):
    str_ing=''.join(map(str,ingredient))
    length=len(str_ing)//4
    cnt=0
    for _ in range(length):
        idx=str_ing.index('1231')
        str_ing=str_ing[idx:]
        cnt+=1
    return cnt

#replace보다는 덜 걸림 77
def solution4(ingredient):
    str_ing=''.join(map(str,ingredient))
    length=len(str_ing)//4
    cnt=0
    for _ in range(length+1):
        if '1231' in str_ing:
            idx=str_ing.index('1231')
            str_ing=str_ing[:idx]+str_ing[idx+4:] 
            cnt+=1
        else:
            break
    return cnt

# 정답
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt
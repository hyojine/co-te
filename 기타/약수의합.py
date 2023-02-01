def solution(n):
    divisor=[]
    for i in range(n):
        # print('1:',i)
        if n%(i+1)==0:
            if i+1 in divisor:
                break
            if i+1 == n//(i+1):
                divisor.append(i+1)
            else: 
                divisor.extend([i+1,n//(i+1)])
    return sum(divisor)

print('답:',solution(144))

#범위를 처음부터 줄여서
def solution2(n):
    divisor=[]
    for i in range(int(n**0.5)):
        # print('2:',i)
        if n%(i+1)==0:
            if i+1 == n//(i+1):
                divisor.append(i+1)
            else: 
                divisor.extend([i+1,n//(i+1)])
    return sum(divisor)

# print(solution2(12))

# def solution3(n):
#     return sum([x + (n//x) if n%x==0 else x if x**0.5==int(x**0.5) for x in range(1,int(n**0.5)+1)])
# # 리스트 축약식으로 제곱근 들어가는 걸 막을 방법이 없나?
# print('답?:',solution3(144))

# 틀림
def solution4(n):
    lam=lambda n: n**0.5 if n**0.5==int(n**0.5) else 0
    # 이렇게하면 n의 제곱근만 나옴
    # lambda n: n을 이 함수의 변수로 사용하겠다
    # :이후는 결과식 먼저, 조건식 다음에 
    # if 문을 쓰면 else도 같이 써줘야하는 것 같음
    # elif도 쓸 수 없음
    # 조건식이 여러개면 그냥 풀어서 쓰는 게 가독성이 더 좋음
    print('lam:',lam(n))

    # <function solution4.<locals>.<lambda> at 0x000001E69068AF80>
    # 실행을 해보면 함수 객체가 나오는데, 이 상태로는 함수를 호출할 수 없습니다. 
    # 왜냐하면 람다 표현식은 이름이 없는 함수를 만들기 때문입니다. 
    # 그래서 람다 표현식을 익명 함수(anonymous function)로 부르기도 합니다.

    listl=[x + (n//x) for x in range(1,int(n**0.5)) if n%x==0]
    listl.append(lam(n))
    print('listl:',listl)
    # 처음에 하려고 한 게
    # sum([x + (n//x) for x in range(1,int(n**0.5)) if n%x==0].append(lam(n)))
    # 이거였는데 
    # TypeError: 'NoneType' object is not iterable 
    # 이런 에러가 뜸 append한건 자체에 값이 저장되니까 append를 한 건 하나의 변수에 저장되는 게 아니라서 sum안에 넣기 전에 실행해서
    # 리스트에 append를 먼저 한 다음에 sum을 해줘야 정상적으로 동작함
    return sum(listl)
# print('답??:',solution4(144))
# 144일땐 답이 맞는데 28일땐 답이 틀림

# 틀림
def solution5(n):
    lam=lambda n: n**0.5 if n**0.5==int(n**0.5) else 0
    listl=[x + (n//x) for x in range(1,int(n**0.5)+1) if n%x==0]
    # 두개씩 들어가서 문제가 되니까 
    # 아래에서 하나 지워준건데 왜 답이 틀리지??
    listl.remove(lam(n))
    # 없어서 못지워줌 애초에 x+n//x로 들어가니까 아래처럼 빼주는 게 맞음
    return sum(listl)

# 정답
def solution6(n):
    lam=lambda n: n**0.5 if n**0.5==int(n**0.5) else 0
    listl=[x + (n//x) for x in range(1,int(n**0.5)+1) if n%x==0 ]
    listl.append(-lam(n))
    return sum(listl)

# print(solution6(12))

# 짧게하려다가 리스트 축약식에서 if문 중첩으로 쓰는 방법 못찾아서 결국 똑같이 해버림ㅋㅋㅋㅋ 그래도 더 짧긴 하넹 ㅋㅅㅋ
iter=[1,2,3,4,5]
res=[x if x>3 else 2 for x in iter]
# 리스트 축약식에서 if else를 쓰려면 이 조건문을 앞에 씀
# print(res)
# 아니그럼?

# 또 1,2,12 번에서 틀림
# 인간승리다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def solution7(n):
    # listl=[x + (n//x) if n%x==0 else x if x==n/x else 0 for x in range(1,int(n**0.5)+1)]
    listl=[x if x==n/x  else x + (n//x) if n%x==0 else 0 for x in range(1,int(n**0.5)+1)]
    print(listl)
    return sum(listl)
print(solution7(12))

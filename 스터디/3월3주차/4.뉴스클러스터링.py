# 영문자로 된 글자 쌍만 유효하고, 
# 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 
# 대문자와 소문자의 차이는 무시
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
import collections

def solution(str1, str2):
    # 배열 만들기
    str1_list,str2_list=[],[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2].lower())  
    # 모두 공집합일 경우 1 리턴
    if str1_list==[] and str2_list==[]:
        return 65536
    # 빈도 카운트 및 계산
    counter_1=collections.Counter(str1_list)
    counter_2=collections.Counter(str2_list)
    numerator,denominator=0,0
    for i in (set(str1_list)&set(str2_list)):
        numerator+=min(counter_1[i],counter_2[i])
    for i in (set(str1_list)&set(str2_list)):
        denominator+=max(counter_1[i],counter_2[i])
    for u in (set(str1_list)-(set(str2_list))):
        denominator+=counter_1[u]
    for u in (set(str2_list)-(set(str1_list))):
        denominator+=counter_2[u]                 
    return int((numerator/denominator)*65536)  
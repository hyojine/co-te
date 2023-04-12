# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 효율성 시간초과
def solution(phone_book):
    answer = True
    for p in phone_book:
        for q in phone_book:
            if len(p)<len(q):
                if q[:len(p)]==p:
                    answer=False
    return answer

# 테스트 14 〉	통과 (154.84ms, 10.1MB)
# 테스트 15 〉	통과 (322.18ms, 10.2MB)
# 테스트 16 〉	통과 (268.53ms, 10.5MB)
# 테스트 17 〉	통과 (388.18ms, 10.3MB)
# 테스트 18 〉	통과 (867.69ms, 10.2MB)
# 테스트 19 〉	통과 (1009.32ms, 10.3MB)
# 테스트 20 〉	통과 (1726.15ms, 10.3MB)

# if len(p)<len(q) and q[:len(p)]==p: # 조건문 두개 and로 변경시

# 테스트 14 〉	통과 (142.89ms, 10.2MB)
# 테스트 15 〉	통과 (273.42ms, 10.4MB)
# 테스트 16 〉	통과 (243.70ms, 10.2MB)
# 테스트 17 〉	통과 (383.78ms, 10.2MB)
# 테스트 18 〉	통과 (695.01ms, 10.4MB)
# 테스트 19 〉	통과 (1272.28ms, 10.4MB)
# 테스트 20 〉	통과 (1337.49ms, 10.2MB)

def solution(phone_book):
    answer = True
    hash_table={}
    for p in phone_book:
        hash_table[hash(p)]=p
    for p in phone_book:
        temp=''
        for l in p:
            temp+=l
            if temp!=p and hash(temp) in hash_table:
                return False
    return answer
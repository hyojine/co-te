# 문자열 s - 영문 대소문자로 구성
# 큰 것부터 작은 순으로 정렬
# 대문자는 소문자보다 작다
# ->새로운 문자열을 리턴
def solution(s):
    return ''.join(sorted(list(s),reverse=True))
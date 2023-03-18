# https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3

def solution(s, skip, index):
    ans=''
    abc=[chr(x) for x in range(ord('a'),ord('z')+1) if chr(x) not in skip]
    for letter in s:
        ans+=abc[(abc.index(letter)+index)%len(abc)]
    return ans
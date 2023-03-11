# https://velog.io/@op032/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98python

# 가장 짧은 변환 과정 구하기
# words에 있는 단어로만, 한 번에 한 개
# 변환할 수 없는 경우에는 0를 return

from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque([[begin, 0]]) # 큐 자료구조를 만들어주고
    # q.append([begin, 0]) # 첫번째 노드를 만들어준다
    visited = [ 0 for _ in range(len(words))] # 노드 방문 여부 표시
    while q: # 요소가 다빠지면 거짓이 되니까 목적지 단어가 큐에 없다면 거짓이 되어 리턴함
        word, cnt = q.popleft() #언패킹 #처음값이 있기때문에 오류x
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]: # 방문한 적이 없는 노드
                for j in range(len(word)): 
                    if word[j] != words[i][j]: # 다른 갯수를 기록
                        temp_cnt += 1
                if temp_cnt == 1: # 하나만 다르면
                    q.append([words[i], cnt+1])
                    visited[i] = 1 # 글자가 하나이상 다르면 방문한적이 없게 되는 것               
    return answer
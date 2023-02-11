# 문자열을 처음부터 자기까지 슬라이스/범위를 그렇게 잡아서
# 같은 글자 인덱스를 뽑아서 리스트에 담고(리스트 축약식) 그중 큰거랑 나랑 인덱스를 빼서담음
def solution(s):
    s=list(s)
    ans=[]
    for idx, letter in enumerate(s):
        idxlist=[]
        for i,same in enumerate(s[0:idx]):
            if same == letter:
                idxlist.append(i)
        if idxlist==[]:
            ans.append(-1)
        else:       
            ans.append(idx-max(idxlist))
    return ans
def solution(t, p):
    plen=len(p)
    count=0
    for i in range(len(t)-plen+1):
        if t[i]<p[0]:
            count+=1
        elif t[i]==p[0]:
            if int(t[i:i+plen])<=int(p):
                count+=1
    return count

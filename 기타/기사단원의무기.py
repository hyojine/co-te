def solution(number, limit, power):
    answer=[] 
    for i in range(1,number+1):
        cnt=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                cnt+=1
        if i**0.5==int(i**0.5):
            cnt=(cnt-1)*2+1
        else:
            cnt=cnt*2
        if cnt>limit:
            cnt=power
        answer.append(cnt)
    return sum(answer)
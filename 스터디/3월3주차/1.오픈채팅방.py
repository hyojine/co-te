def solution(record):
    record=[re.split(' ') for re in record]
    id_nick={}
    answer=[]
    for re in reversed(record):
        if re[1] not in id_nick.keys() and re[0] !='Leave':
                id_nick[re[1]]=re[2]
    for re in record:
        if re[0]=='Enter':
            answer.append(id_nick[re[1]]+'님이 들어왔습니다.')
        elif re[0]=='Leave':
            answer.append(id_nick[re[1]]+'님이 나갔습니다.')
    return answer
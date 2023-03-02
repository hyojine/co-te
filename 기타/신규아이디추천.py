def solution(new_id):
    new_id=''.join([x for x in new_id.lower() if x not in '~!@#$%^&*()=+[{]}:?,<>/'])
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    if new_id[0]=='.' and new_id[-1]=='.':
        new_id=new_id[1:-1]
    elif new_id[-1]=='.':# 둘 다 있을 수도 있음
        new_id=new_id[:-1]
    elif new_id[0]=='.':
        new_id=new_id[1:]
    if new_id =='':
        new_id='a'   
    if len(new_id)>=16: # 안하고 그냥 슬라이싱해도 됨
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    if len(new_id)<3:
        new_id+=new_id[-1]*(3-len(new_id))
    return new_id
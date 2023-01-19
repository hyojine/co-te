a=sorted(list('21234'))
print(a)
print(sorted(list('21234'),reverse=True))

def solution(n):
    return int(''.join(sorted(list(str(n)),reverse=True)))

a=129384
a_list=list(map(int,str(a)))
b_list=[]
for i in range(len(a_list)):
    b_list.append(a_list.pop(a_list.index(max(a_list))))
print(b_list)
b_list=list(map(str,b_list))
print('--',b_list)
print(''.join(b_list))
print(type(b_list))

# 2번째
def solution(n):
    n_list=list(map(int,str(n)))
    new_list=[]
    for i in range(len(n_list)):
        new_list.append(n_list.pop(n_list.index(max(n_list))))
    new_list=list(map(str,new_list))
    return int(''.join(new_list))
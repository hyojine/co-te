# a=123
# print([a])
# print(str(a))
# print(list(a))# 'int' object is not iterable

# 계속 %10해서 한자리수를 뺄 수는 있쥬?

# print(int('0000')) #0
num_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in num_dict.keys():
    print(i)

# 시간초과
def solution(X, Y):
    num_dict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for fac in str(X):
        for num in num_dict.keys():
            if num==fac:
                num_dict[num]+=1
    num_dict2={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for fac in str(Y):
        for num in num_dict2.keys():
            if num==fac:
                num_dict2[num]+=1
    ans=[]
    for num in list(num_dict.keys()):
        if num_dict[num]==0 or num_dict2[num]==0:
            continue
        else:
            ans.append(num*min(num_dict[num],num_dict2[num]))
    if ans==[]:
        return '-1'
    if int(''.join(reversed(ans))) == 0:
        return '0'
    return ''.join(reversed(ans))
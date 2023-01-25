# a='01093213915'
# for i in range(len(a[:-4])) :
#     a.replace(a[i],'*') # 값을 값으로 바꿈
#     print(a.replace(a[i],'*'))
# for i in range(len(a[:-4])) :
#     a[i]='*' # assignment안됨

# repeated='*'*len(a[:-4])
# print(a.replace(a[:-4],repeated))

def solution(phone_number):
    repeated='*'*len(phone_number[:-4])
    return phone_number.replace(phone_number[:-4],repeated)

print(solution('078109622298145'))


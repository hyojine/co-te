# 시간초과남
# def solution(n):
#     p_cnt=0
#     for i in range(2,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count ==2:
#             p_cnt+=1
#     return p_cnt

# 통과
# def solution(n):
#     p_cnt=0
#     for i in range(2,n+1):
#         count=0 
#         for j in range(1,int(i**(0.5))+1):
#             if i%j==0:
#                 count+=1
#             if count>1:
#                 break
#         if count ==1:
#             p_cnt+=1
#     return p_cnt

# 여기서
# if i**0.5 == round(i,1):로 걸러주면 더 오래걸림
def solution(n):
    p_cnt=0
    for i in range(2,n+1):
        count=0 
        if i**0.5 != round(i**0.5,1):
            for j in range(1,int(i**(0.5))+1):
                if i%j==0:
                    count+=1
                if count>1:
                    break
            if count ==1:
                p_cnt+=1
    return p_cnt                

print(solution(10))

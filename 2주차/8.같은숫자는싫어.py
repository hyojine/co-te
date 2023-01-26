# def solution(arr):
#     # if len(arr)==1:
#     #     pass
#     # if len(arr)>1:
#     for i in range(1,len(arr)+1):
#         print(i)
#         if arr[i]==arr[i-1]:
#             arr.remove(arr[i])
#     return arr

# print(solution([1, 1, 3, 3, 0, 1, 1]))
# 같은 숫자를 삭제하다 보니까 리스트 길이가 짧아져서 ..
# IndexError: list index out of range

# exp2
# 0-9 까지의 배열을 만들고
# 그 배열 안의 요소가 리스트를 스트링으로 바꾼 값에 여러개 있으면 하나로 바꾸는
# arr=[1, 1, 3, 3, 0, 1, 1]
# print("".join(arr))
# 배열 안의 요소가 모두 int라서 join을 쓸 수 없음

# exp3
# n의 길이의 배열이 포함되어있으면 그 길이를 1로 바꿈
# print([1]*5)

# exp4
# def solution(arr):
#     idx=[]
#     for i in range(len(arr)-1):
#         print(i)
#         if arr[i]==arr[i+1]:
#             idx.append(i)
#     for i in idx:
#         arr.pop(i)
#     return arr
# 인덱스를 저장해뒀다가 나중에 빼도 결과는 처음에 했던거랑 똑같은
# IndexError: pop index out of range
arr=[4,4,4,3,3]

# 효율성 테스트 통과 못함
# def solution(arr):
#     int_to_str=list(map(str,arr))
#     arr_to_str=''.join(int_to_str)
#     for i in arr_to_str:
#         for n in range(2,len(arr)):
#             if i*n in arr_to_str:
#                 arr_to_str=arr_to_str.replace(i*n,i)
#     str_to_int=list(map(int,arr_to_str))
#     return str_to_int

# 효율성 테스트 통과 못함2
def solution(arr):
    if len(arr)>1:
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1]:
                arr[i]='x'
    while 'x' in arr:
        arr.remove('x')
    return arr

print(solution(arr))
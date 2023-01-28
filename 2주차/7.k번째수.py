def solution(array, commands):
    ans=[]
    for i in range(len(commands)):
        slice=sorted(array[commands[i][0]-1:commands[i][1]])
        ans.append(slice[commands[i][2]-1])
    return ans

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))
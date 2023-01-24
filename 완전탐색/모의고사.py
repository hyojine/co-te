# thislist=[2,3,4,3,3,5,6,6]
# print(thislist.index(max(thislist)))
# print(sorted(thislist))
# a=thislist.sort() #[2, 3, 3, 3, 4, 5, 6, 6]
# print(a) #None

def solution(answers):
    student = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_cnt={}
    for i in range(len(student)):
        count=0
        while len(student[i])<len(answers):
            student[i].extend(student[i])
        if len(student[i])-len(answers):
            student[i]=student[i][:-(len(student[i])-len(answers))]
        for num in range(len(student[i])):
            if student[i][num]==answers[num]:
                count+=1
        answer_cnt[i+1]=count
    ans=[k for k,v in answer_cnt.items() if max(answer_cnt.values())==v]
    return ans

# 다르게
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# 처음에 하려고 했던거
def solution(answers):
    student = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]

    for i in range(len(student)):
        print(len(student))
        if len(answers)%len(student[i])==0:
            for n in range(len(answers)//len(student[i])):
                for idx in range(len(student[i])):
                    if student[i][idx]==answers[len(student[i])*n+idx]:
                        score[i]+=1
        else:
            for n in range(len(answers)//len(student[i])+1):
                for idx in range(len(student[i])):
                    if student[i][idx]==answers[len(student[i])*n+idx]:
                        score[i]+=1
                    if len(student[i])*n+idx == len(answers)-1:
                        print(len(student[i])*n+idx, len(answers)-1)
                        break 
    result=[]
    for idx,value in enumerate(score):
        idx+=1
        if value == max(score):
            result.append(idx)
    return result

print(solution([1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]))
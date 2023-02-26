def solution(survey, choices):
    default='RCJA'
    default2='TFMN'
    ans={}
    for i,cho in enumerate(choices):
        if survey[i][1] in ans.keys():
            if cho>4:
                ans[survey[i][1]]+=cho-4
            elif cho<4:
                ans[survey[i][0]]+=4-cho
        else:
            if cho>4:
                ans[survey[i][0]]=0
                ans[survey[i][1]]=cho-4
            elif cho<4:
                ans[survey[i][0]]=4-cho
                ans[survey[i][1]]=0
    for i in range(4):
        if default[i] in ans.keys():
            if ans[default2[i]]>ans[default[i]]:
                default=default.replace(default[i],default2[i])
    return default

# 설문_조사_배열=["AN", "CF", "MJ", "RT", "NA"]
# for i in range(len(설문_조사_배열)):
#         비동의_캐릭터, 동의_캐릭터 = 설문_조사_배열[i]
#         print(비동의_캐릭터, 동의_캐릭터)

def solution(survey, choices):
    scores = {"R":0, "T":0, "C":0, "F":0,"J":0, "M":0 ,"A":0, "N":0}
    ans=''
    for i,cho in enumerate(choices):
            if cho>4:
                scores[survey[i][1]]+=cho-4
            elif cho<4:
                scores[survey[i][0]]+=4-cho
    for i in range(0,8,2):
        if list(scores.values())[i]>=list(scores.values())[i+1]:
            ans+=list(scores.keys())[i]
        else:
            ans+=list(scores.keys())[i+1]
    return ans

# 한글 코딩 복사
# def solution(설문_조사_배열, 선택지_배열):
#     지표 = {}
#     지표['RT'] = 지표['TR'] = {'R': 0, 'T': 0,}
#     지표['FC'] = 지표['CF'] = {'C': 0, 'F': 0,}
#     지표['MJ'] = 지표['JM'] = {'J': 0, 'M': 0,}
#     지표['AN'] = 지표['NA'] = {'A': 0, 'N': 0,}
#     점수 = {
#         '매우 비동의': 3,
#         '비동의': 2,
#         '약간 비동의': 1,
#         '모르겠음': 0,
#         '약간 동의': 1,
#         '동의': 2,
#         '매우 동의': 3,
#     }
#     비동의 = [1, 2, 3]
#     동의 = [5, 6, 7]
#     선택지 = {
#         1: '매우 비동의',
#         2: '비동의',
#         3: '약간 비동의',
#         4: '모르겠음',
#         5: '약간 동의',
#         6: '동의',
#         7: '매우 동의',
#     }

#     for 인덱스 in range(len(설문_조사_배열)):
#         비동의_캐릭터, 동의_캐릭터 = 설문_조사_배열[인덱스]

#         if 선택지_배열[인덱스] in 비동의:
#             지표[설문_조사_배열[인덱스]][비동의_캐릭터] += 점수[선택지[선택지_배열[인덱스]]]
#             continue

#         if 선택지_배열[인덱스] in 동의:
#             지표[설문_조사_배열[인덱스]][동의_캐릭터] += 점수[선택지[선택지_배열[인덱스]]]

#     결과_배열 = [지표['RT'].items(), 지표['FC'].items(), 지표['MJ'].items(), 지표['AN'].items()]
#     정렬된_배열 = []

#     for 결과 in 결과_배열:
#         정렬된_배열.append(sorted(결과, key=lambda x: -x[1]))

#     print(지표)
#     return ''.join([캐릭터_점수_튜플[0] for [캐릭터_점수_튜플, _] in 정렬된_배열])


print(solution(["TR", "RT", "TR"],[7, 1, 3]))
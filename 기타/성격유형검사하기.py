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
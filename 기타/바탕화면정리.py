# 정확성: 80.6
def solution(wallpaper):
    answer = []
    for row in wallpaper:
        for i in row:
            if i=='#':
                answer.append((wallpaper.index(row),row.index(i)))
                break         
        for i in row[::-1]:
            if i=='#':
                answer.append((wallpaper.index(row),len(row)-row[::-1].index(i)-1))
                break
    x=[x[0] for x in answer]
    y=[x[1] for x in answer]  
    return [min(x),min(y),max(x)+1,max(y)+1]

#통과
def solution(wallpaper):
    answer = []
    for ir,row in enumerate(wallpaper):
        for id,i in enumerate(row):
            if i=='#':
                answer.append((ir,id))
    x=[x[0] for x in answer]
    y=[x[1] for x in answer]  
    return [min(x),min(y),max(x)+1,max(y)+1]
def solution(a, b):
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    week=['THU','FRI','SAT','SUN','MON','TUE','WED',]
    idx=(sum(days[:a-1])+b)%7
    print(days[:a],week[idx])
    return week[idx]

import datetime

def solution(a, b):
    days=['MON','TUE','WED','THU','FRI','SAT','SUN']
    return days[datetime.date(2016,a,b).weekday()]
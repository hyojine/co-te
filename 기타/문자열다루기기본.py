def solution(s):
    numbers='0123456789'
    return (len(s)==4 or len(s)==6) and (len([x for x in s if x in numbers])==len(s))

def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            try: 
                int(i)
            except:
                return False
        return True
    else:
        return False        

def solution(s):
    return s.isdigit() and len(s) in (4,6)
    # str.isnumeric()
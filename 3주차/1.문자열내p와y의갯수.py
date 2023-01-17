def solution(s):
    s=s.lower()
    if 'p' or 's' in list(s):
        if list(s).count('p') == list(s).count('y'):
            return True
        else:
            return False
    else:
        return True
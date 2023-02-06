def solution(s):
    letters=['zero','one','two','three','four','five','six','seven','eight','nine']
    for letter in letters:
        if letter in s:
            for i in range(s.count(letter)):
                s=s.replace(letter,str(letters.index(letter)))
    return int(s)

def solution(s):
    letters=['zero','one','two','three','four','five','six','seven','eight','nine']
    for letter in letters:
        if letter in s:
            s=s.replace(letter,str(letters.index(letter)),s.count(letter))
    return int(s)

print(solution('threethreethree'))
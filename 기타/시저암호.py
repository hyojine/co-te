def solution(s, n):
    ans=[]
    for letter in s:
        if ord(letter) in range(65,91) or ord(letter) in range(97,123):
            idx=ord(letter)+n
            if letter.islower():
                if idx>122:
                    idx-=26
            else:
                if idx>90:
                    idx-=26
            ans.append(chr(idx))
        else:
            ans.append(letter)       
    return ''.join(ans)

def solution(s, n):
    ans=[]
    for letter in s:
        if not letter.isalpha():
            ans.append(letter)
        else:
            idx=ord(letter.upper())+n
            if idx>90:
                idx-=26
            if letter.islower():
                ans.append(chr(idx).lower())
            else:
                ans.append(chr(idx))
    return ''.join(ans)

def solution(s, n):
    ans=[]
    for letter in s:
        if not letter.isalpha():
            ans.append(letter)
        else:
            idx=(ord(letter.upper())-ord('A')+n)%26+ord('A')
            if letter.islower():
                ans.append(chr(idx).lower())
            else:
                ans.append(chr(idx))
    return ''.join(ans)

def solution(s, n):
    s=list(s)
    for i,letter in enumerate(s):
        if letter.isalpha():
            idx=(ord(letter.upper())-ord('A')+n)%26+ord('A')
            if letter.islower():
                s[i]=(chr(idx).lower()) #s[i]대신 letter을 쓰면 틀림
            else:
                 s[i]=(chr(idx))
    return ''.join(s)

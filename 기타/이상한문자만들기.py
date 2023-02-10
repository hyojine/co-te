def solution(s):
    word_list=s.split() #공백이 하나 이상인 경우는 이게 맞는 것 같은데..
    for idx,word in enumerate(word_list):
        # cnt=0
        for i,letter in enumerate(word):
            if i%2==0:
                word=word.replace(letter,letter.upper(),1)
            else:
                word=word.replace(letter,letter.lower(),1)
        word_list[idx]=word
    return ' '.join(word_list)

s="try        hello world "

def solution2(s):
    word_list=s.split(' ')
    new_word_list=[]
    for word in word_list:
        new_word=''
        for idx in range(len(word)):
            if idx%2==0:
                new_word+=word[idx].upper()
            else:
                new_word+=word[idx].lower()
        new_word_list.append(new_word)
    return ' '.join(new_word_list)

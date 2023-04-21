# https://www.acmicpc.net/problem/1157

alphabet_list = input().upper()
alphabet_set = list(set(alphabet_list.upper()))
cnt = []
for i in range(len(alphabet_set)):
    cnt.append(alphabet_list.count(alphabet_set[i]))
    # print(alphabet_list.count(alphabet_set[i])) 
if cnt.count(max(cnt)) != 1:
    print('?')
else:
    print(alphabet_set[cnt.index(max(cnt))])
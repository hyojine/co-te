def solution(strings, n):
    key_list=[x[n] for x in strings]
    return [y[1] for y in (sorted([x for x in zip(key_list,strings)]))]
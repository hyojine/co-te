def solution(participant, completion):
    if len(participant)==len(set(participant)):
        return (set(participant)-set(completion)).pop()
    else:
        for i,j in zip(sorted(participant),sorted(completion)):
            if i != j:
                return i

def solution(participant, completion):
    for i,j in zip(sorted(participant),sorted(completion)):
            if i != j:
                return i
    return sorted(participant)[-1]
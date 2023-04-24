# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = -1
    DP = [[] for _ in range(9)]
    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        for j in range(1, (i+1)//2):
            for x in DP[j]:
                for y in DP[i-j]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(y - x)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)
                    if x != 0:
                        numbers.add(y // x)
        if number in numbers:
            answer = i
            break
        DP[i]=numbers
        # DP.append(numbers)
    print(DP)
    return answer

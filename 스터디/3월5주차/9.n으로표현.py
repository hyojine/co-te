# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = -1
    DP = []
    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        for j in range(0, i//2):
            for x in DP[j]:
                for y in DP[-j-1]:
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
        DP.append(numbers)

    return answer
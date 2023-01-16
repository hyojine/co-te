def solution(numbers):
    total=sum([0,1,2,3,4,5,6,7,8,9])
    for i in numbers:
        total = total -i
    return total

# 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지
def solution(a, b, n):
    bottles=[(n//a)*b] # 가장 처음에 받은 병 수
    x=(n//a)*b+n%a #이후 내가 가지고 있는 총 콜라병 갯수
    while x>=a:
        bottles.append((x//a)*b)
        x=(x//a)*b+x%a
    return sum(bottles)
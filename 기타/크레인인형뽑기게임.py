def solution(board, moves):
    basket=[0]
    cnt=0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                match=basket[-1]
                basket.append(board[i][move-1])
                board[i][move-1]=0
                if match!=0 and match==basket[-1]:
                    basket=basket[:-2]
                    cnt+=1
                break
    return cnt*2
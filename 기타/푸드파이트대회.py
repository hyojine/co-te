def solution(food):
    food.pop(0)
    # for f in range(len(food)):
    #     if food[f]//2!=0:
    #         food[f]=(food[f]//2)*str(f+1)
    # food=[x for x in food if x!=1]
    food=[x for x in [(x//2)*str(i+1) for i,x in enumerate(food) if x != 1] if x != 0]
    food.append('0')
    food.extend(reversed(food[:-1]))
    return ''.join(food)

def solution2(food):
    food=[(x//2)*str(i) for i,x in enumerate(food) if x != 1]
    food.append('0')
    food.extend(food[-2::-1])
    return ''.join(food)

print([x for x in range(4,0,-1)])

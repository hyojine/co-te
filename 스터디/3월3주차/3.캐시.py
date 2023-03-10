from collections import OrderedDict

def solution(cacheSize, cities):
    frequency=OrderedDict()
    hit, miss = 0, 0
    for city in cities:
        city=city.lower()
        if city not in frequency.keys():
            miss+=1
            frequency[city]=1  
            if cacheSize<len(frequency):
                least=list(frequency.keys())[0]
                del frequency[least]
        else:
            frequency[city]+=1
            frequency.move_to_end(city,last=True)
            hit+=1
    return hit*1+miss*5
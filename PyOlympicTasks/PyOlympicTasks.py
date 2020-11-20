import math
import operator
import copy
from random import shuffle
##################################################
def spider_search(cities, start, end):
    global short_cut
    global cut_is_real
    global distance
    if(start == end):
        short_cut = 0
        cut_is_real = True
        return 1
    last_cities = []
    cities[start]['ban']=True
    last_cities.append(start)
    size = 0
    while(not cut_is_real):
        error = True
        new_last_cities = []
        for i in last_cities:
            for j in cities:
                if cities[j]['ban']: continue
                if (abs(cities[i]['y'] - cities[j]['y']) + abs(cities[i]['x'] - cities[j]['x'])) > distance: continue
                if j == end:
                    short_cut = size + 1
                    cut_is_real = True
                    error = False
                    return 1
                else:
                    error = False
                    cities[j]['ban']=True
                    new_last_cities.append(j)
        if(error):break
        size = size + 1
        last_cities = new_last_cities
    return -1
##################################################
cityNumbers = int(input())
cities = {}
for i in range(cityNumbers):
    coord = input().split()
    City = {'x':int(coord[0]),
            'y':int(coord[1]),
        'ban':False}
    cities[i] = (City)
distance = int(input())
first_last = input().split()
first = int(first_last[0])
last = int(first_last[1])
path = []
short_cut = cityNumbers
cut_is_real = False
result = spider_search(cities,first - 1,last - 1)
if cut_is_real: print(short_cut)
else: print(-1)
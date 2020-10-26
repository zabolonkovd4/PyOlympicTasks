import math
import operator
import copy
from random import shuffle

##################################################
def recursive_search(cities, old_data, size, now, end, max):
    global short_cut
    global cut_is_real
    if (now == end):
        cut_is_real = True
        short_cut = size
        return size
    if (size + 1) > short_cut: return -1
    old_data.append(now)
    results = []
    for i in cities[now]['neighbors']:
        tr = False
        for j in old_data:
            if i == j:
                tr = True
                break
        if tr:
            continue
        size_local = search(cities,old_data,size + 1, i, end, max)
        results.append(size_local)
    result = max
    for i in results:
        if i == -1: continue
        if i < result: result = i
    if result == max: return -1
    else:
        cut_is_real = True
        short_cut = result
        return result
##################################################
def list_search(cities, path, size, now, end, max):
    global short_cut
    global cut_is_real
    path.append(now)
    cut = True
    while(cut):
        print(path)
        cut = False
        if(now == end):
            if(size < short_cut): short_cut = size
            cut_is_real = True
            if(not cut and len(path) > 1):
                path.pop()
                now = path[len(path) - 1]
                size = size - 1
                cut = True
        for i in cities[now]['neighbors']:
            if i['index'] in path:continue
            if size in cities[i['index']]['ban']:continue
            if((size + 1) >= short_cut):continue
            cities[i['index']]['ban'].append(size)
            size = size + 1
            cut = True
            now = i['index']
            path.append(now)
            break
        if(not cut and len(path) > 1):
            path.pop()
            now = path[len(path) - 1]
            size = size - 1
            cut = True
    return size
##################################################
def spider_search(cities, now, end):
    global short_cut
    global cut_is_real
    if(now == end):
        short_cut = 0
        cut_is_real = True
        return 1
    cities_visited = []
    cities_visited.append(now)
    all_paths = []
    for i in cities[now]['neighbors']:
        if i==end:
            short_cut = 1
            cut_is_real = True
            return 1
        cities_visited.append(i)
        path = [now,i]
        all_paths.append(path)
    size = 1
    while(not cut_is_real):
        error = True
        new_all_paths = []
        for i in all_paths:
            for j in cities[i[len(i) - 1]]['neighbors']:
                if j in i:continue
                if j in cities_visited:continue
                if j == end:
                    short_cut = size + 1
                    cut_is_real = True
                    error = False
                    return 1
                else:
                    error = False
                    ii = copy.deepcopy(i)
                    ii.append(j)
                    cities_visited.append(j)
                    new_all_paths.append(ii)
        if(error):break
        size = size + 1
        all_paths=new_all_paths
    return -1
##################################################

##################################################

def create_graph(cityNumbers, cities, distance):
    for i in range(cityNumbers):
        for k in range(cityNumbers):
            if i == k: continue
            R = abs(cities[i]['y'] - cities[k]['y']) + abs(cities[i]['x'] - cities[k]['x'])
            neig = {'R':R, 'index':k}
            if R <= distance: cities[i]['neighbors'].append(k)
    return cities

cityNumbers = int(input())
cities = []
for i in range(cityNumbers):
    coord = input().split()
    City = {'x':int(coord[0]),
            'y':int(coord[1]),
            'index':i,
        'neighbors':[],
        'ban':[]}
    cities.append(City)
distance = int(input())
first_last = input().split()
first = int(first_last[0])
last = int(first_last[1])

cities = create_graph(cityNumbers, cities, distance)

path = []
short_cut = cityNumbers
cut_is_real = False
#result = recursive_search(cities,path,0, first - 1,last - 1,cityNumbers)
#result = list_search(cities,path,0, first - 1,last - 1,cityNumbers)
result = spider_search(cities,first - 1,last - 1)
if cut_is_real: print(short_cut)
else: print(-1)
import math
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
        cut = False
        if(now==end):
            if(size<short_cut): short_cut=size
            cut_is_real = True
            if(not cut and len(path)>1):
                path.pop()
                now = path[len(path)-1]
                size=size-1
                cut=True
        for i in cities[now]['neighbors']:
            if i in path:continue
            if size in cities[i]['ban']:continue
            else:
                if((size+1)>short_cut):continue
                else:
                    cities[i]['ban'].append(size)
                    size=size+1
                    cut = True
                    now = i
                    path.append(now)
                    break
        if(not cut and len(path)>1):
            path.pop()
            now = path[len(path)-1]
            size=size-1
            cut=True
    return size
##################################################
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
distance = int(pow(distance,2))
first_last = input().split()
first = int(first_last[0])
last = int(first_last[1])

for i in range(cityNumbers):
    for k in range(cityNumbers):
        if i == k: continue
        R = int(math.pow((cities[i]['y'] - cities[k]['y']),2) + math.pow((cities[i]['x'] - cities[k]['x']),2))
       # R = math.sqrt(R)
        if R <= distance: cities[i]['neighbors'].append(k)
path = []
short_cut = cityNumbers
cut_is_real = False
#result = recursive_search(cities,path,0, first - 1,last - 1,cityNumbers)
result = list_search(cities,path,0, first - 1,last - 1,cityNumbers)
if cut_is_real: print(short_cut)
else: print(-1)
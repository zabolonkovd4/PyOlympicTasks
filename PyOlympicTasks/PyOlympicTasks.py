import math

def search(cities, old_data, size, now, end, max):
    if (now == end):
        return size
    global short_cut
    global cut_is_realy
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
        cut_is_realy = True
        short_cut = result
        return result
##################################################
cityNumbers = int(input())
cities = []
for i in range(cityNumbers):
    coord = input().split()
    City = {'x':int(coord[0]),
         'y':int(coord[1]),
         'index':i,
        'neighbors':[]}
    cities.append(City)
distance = int(input())
first_last = input().split()
first = int(first_last[0])
last = int(first_last[1])

for i in range(cityNumbers):
    for k in range(cityNumbers):
        if i == k: continue
        R = math.pow((cities[i]['y'] - cities[k]['y']),2) + math.pow((cities[i]['x'] - cities[k]['x']),2)
        R = math.sqrt(R)
        if R <= distance: cities[i]['neighbors'].append(k)
old_data = []
short_cut = cityNumbers
cut_is_realy = False
result = search(cities,old_data,0, first - 1,last - 1,cityNumbers)
if cut_is_realy: print(short_cut)
else: print(-1)
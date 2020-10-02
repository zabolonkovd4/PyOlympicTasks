def search(cities, old_data, size, now, end, max):
    if (now == end):
        return size
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
        error = False
        size_local = search(cities,old_data,size + 1, i, end, max)
        results.append(size_local)
    if error:
        return -1
    else:
        result = max
        for i in results:
            if i == -1: continue
            if i < result: result = i
        if result==max: return -1
        else: return result

##################################################
#############MAIN#################################
cityNumbers = int(input())
cities = []
for i in range(cityNumbers):
    coord = input().split()
    City={'x':int(coord[0]),
         'y':int(coord[1]),
         'index':i,
        'neighbors':[]}
    cities.append(City)
distance = int(input())
distance= distance*distance
first_last = input().split()
first = int(first_last[0])
last = int(first_last[1])

for i in range(cityNumbers):
    for k in range(cityNumbers):
        if i==k: continue
        R = (cities[i]['y'] - cities[k]['y']) * (cities[i]['y'] - cities[k]['y']) + (cities[i]['x'] - cities[k]['x']) * (cities[i]['x'] - cities[k]['x'])
        if R <= distance: cities[i]['neighbors'].append(k)
old_data = []
result = search(cities,old_data,0, first-1,last-1,cityNumbers)
print(result)
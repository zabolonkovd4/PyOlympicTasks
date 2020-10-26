import unittest
import math
import copy
def spider_search(cities, now, end,short_cut,cut_is_real):
    if(now == end):
        short_cut = 0
        cut_is_real = True
        return 1,short_cut,cut_is_real
    cities_visited = []
    cities_visited.append(now)
    all_paths = []
    for i in cities[now]['neighbors']:
        if i==end:
            short_cut = 1
            cut_is_real = True
            return 1,short_cut,cut_is_real
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
                    return 1,short_cut,cut_is_real
                else:
                    error = False
                    ii = copy.deepcopy(i)
                    ii.append(j)
                    cities_visited.append(j)
                    new_all_paths.append(ii)
        if(error):break
        size = size + 1
        all_paths=new_all_paths
    return -1,short_cut,cut_is_real
def create_graph(cityNumbers, cities, distance):
    for i in range(cityNumbers):
        for k in range(cityNumbers):
            if i == k: continue
            R = abs(cities[i]['y'] - cities[k]['y']) + abs(cities[i]['x'] - cities[k]['x'])
            if R <= distance: cities[i]['neighbors'].append(k)
    return cities
def search(cities, now, end , short_cut,cut_is_real):
    result,short_cut,cut_is_real = spider_search(cities,now -1, end-1,short_cut,cut_is_real)
    if cut_is_real: return short_cut
    else: return -1
def my_test(cityNumbers,coords,distance,first,last):
    cities=[]
    for i in range(cityNumbers):
        City = {'x':int(coords[i][0]),
        'y':int(coords[i][1]),
        'index':i,
        'neighbors':[],
        'ban':[]}
        cities.append(City)        
    cities = create_graph(cityNumbers, cities, distance)    
    short_cut = cityNumbers
    cut_is_real = False
    result = search(cities,first, last,short_cut,cut_is_real)
    return result
class Test_test_2(unittest.TestCase):
    def test_A(self):        
        cityNumbers =7
        coords = [[0,0],
                  [0,2], 
                  [2,2], 
                  [0,-2], 
                  [2,-2], 
                  [2,-1], 
                  [2,1]]
        distance = 2
        first =1
        last = 3
        result = my_test(cityNumbers,coords, distance,first,last)
        self.assertEqual(result, 2)
###################################
    def test_B(self):        
        cityNumbers = 4
        coords = [[0,0],
                  [1,0], 
                  [0,1], 
                  [1,1]]
        distance = 2
        first =1
        last = 4
        result = my_test(cityNumbers,coords, distance,first,last)
        self.assertEqual(result, 1)
###################################
    def test_C(self):        
        cityNumbers = 4
        coords = [[0,0],
                  [2,0], 
                  [0,2], 
                  [2,2]]
        distance = 1
        first =1
        last = 4
        result = my_test(cityNumbers,coords, distance,first,last)
        self.assertEqual(result, -1)
        ###################################
    def test_D(self):        
        cityNumbers = 6
        coords = [[0,0],[0,-1e9],[0,1e9],[0,1],[0,2],[-1,-1]]
        distance = 2e9
        first =2
        last = 3
        result = my_test(cityNumbers,coords, distance,first,last)
        self.assertEqual(result, 1)
        ###################################
    def test_H(self):        
        cityNumbers = 1000
        coords = []
        for i in range(cityNumbers):
            cor=[0,i]
            coords.append(cor)
        distance = 1
        first =1
        last = cityNumbers
        result = my_test(cityNumbers,coords, distance,first,last)
        self.assertEqual(result, cityNumbers-1)


if __name__ == '__main__':
    unittest.main()

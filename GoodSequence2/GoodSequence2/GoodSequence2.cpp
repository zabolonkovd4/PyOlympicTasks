#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
enum class Parity { Even, Odd };

struct Point {
    int x;
    int y;
    int z;
};

Parity operator+ (Parity parity, std::size_t count)
{
    return static_cast<Parity>((static_cast<std::size_t>(parity) + count) % 2);
}

template<typename It>
bool next_permutation(It begin, It end, Parity& parity)
{
    if (begin == end)
        return false;

    It i = begin;
    ++i;
    if (i == end)
        return false;

    i = end;
    --i;

    while (true)
    {
        It j = i;
        --i;

        if (*i < *j)
        {
            It k = end;

            while (!(*i < *--k))
                /* pass */;

            std::iter_swap(i, k);
            parity = parity + 1;
            std::reverse(j, end);
            parity = parity + std::distance(j, end) / 2;
            return true;
        }

        if (i == begin)
        {
            std::reverse(begin, end);
            parity = parity + std::distance(begin, end) / 2;
            return false;
        }
    }
}

int Convex(vector<Point> points)
{
    int j, k;
    int flag = 0;
    double z;

    int a1 = 0;
    int a2 = 0;
    int a3 = 0;

    if (points.size() < 3)
        return(0);

    for (int i = 0; i < points.size(); i++) {
        j = (i + 1) % points.size();
        k = (i + 2) % points.size();
        z = (points[j].x - points[i].x) * (points[k].y - points[j].y);
        z -= (points[j].y - points[i].y) * (points[k].x - points[j].x);
        if (z == 0) return(-1);
        else if (z < 0)
            flag |= 1;
        else if (z > 0)
            flag |= 2;
        if (flag == 3)
        {
            a1 = 1;
        }
    }
    flag = 0;
    for (int i = 0; i < points.size(); i++) {
        j = (i + 1) % points.size();
        k = (i + 2) % points.size();
        z = (points[j].x - points[i].x) * (points[k].z - points[j].z);
        z -= (points[j].z - points[i].z) * (points[k].x - points[j].x);
        if (z == 0) return(-1);
        else if (z < 0)
            flag |= 1;
        else if (z > 0)
            flag |= 2;
        if (flag == 3)
            a2 = 1;
    }
    flag = 0;
    for (int i = 0; i < points.size(); i++) {
        j = (i + 1) % points.size();
        k = (i + 2) % points.size();
        z = (points[j].y - points[i].y) * (points[k].z - points[j].z);
        z -= (points[j].z - points[i].z) * (points[k].y - points[j].y);
        if (z == 0) return(-1);
        else if (z < 0)
            flag |= 1;
        else if (z > 0)
            flag |= 2;
        if (flag == 3)
            a3 = 1;
    }

    if (a1 == a2 == a3 == 1)
        return(-1);

    else if (flag != 0)
        return(1);
    else
        return(0);
}

int main()
{
    int n;
    cin >> n;
    vector<Point> points(0);
    for (int i = 0; i < n; i++)
    {
        Point p;
        cin >> p.x >> p.y >> p.z;
        points.emplace_back(p);
    }

    vector<int> indexes(points.size());
    vector<Point> points2(points.size());
    for (int i = 0; i < indexes.size(); i++)
        indexes[i] = i;

    int i = 0;
    Parity parity = Parity::Even;

    do 
    {
        if (parity == Parity::Even)
        {
            for (int i = 0; i < points2.size(); i++)
                points2[i] = points[indexes[i]];

            int ddd = Convex(points2);
            if (ddd == -1) // -1 - не выпуклая
                break;
        }
        i++;
    } while (::next_permutation(indexes.begin(), indexes.end(), parity));

    for (int i = 0; i < indexes.size(); i++)
        cout << indexes[i] + 1 << " ";

    return 0;
}

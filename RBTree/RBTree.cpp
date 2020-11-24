#include <iostream>
using namespace std;
class rb_tree
{
public:
    int countRed(int i, int h, int N);
    int countBlack(int i, int h, int N);
};

int rb_tree::countRed(int i, int h, int N)
{
    int j = N - i;
    if (i < 1) return 0;
    if (i - 1 < j)
    {
		int countLeft = countBlack(i - 1, h, N);
		int countRight = countBlack(j, h, N);
        return countLeft * countRight;
    }
    if (i - 1 == j)
    {
		int countLeft = countBlack(i - 1, h - 1, N) + countRed(i - 1, h - 1, N);
        return countLeft * (countLeft + 1) / 2;
    }
    if (i - 1 > j)
        cout << "ebanina" << endl; return 0;
}

int rb_tree::countBlack(int i, int h, int N)
{
    int j = N - i;
    if (i < 1) return 0;
    if (i - 1 < j)
    {
		int countLeft = countBlack(i - 1, h - 1, N) + countRed(i - 1, h - 1, N);
		int countRight = countBlack(j, h - 1, N) + countRed(j, h - 1, N);
        return countLeft * countRight;
    }
    if (i - 1 == j)
    {
		int countLeft = countBlack(i - 1, h - 1, N) + countRed(i - 1, h - 1, N);
        return countLeft * (countLeft + 1) / 2;
    }
    if (i - 1 > j)
        cout << "ebanina" << endl; return 0;
}

int main()
{
    rb_tree rb;
    unsigned int n;
    std::cin >> n;
    unsigned int h = 2 * log2(n);

    int lastSum = 0;
    int maxI = (n + 1) / 2;
    for (int hh = 1; hh < 20; hh++)
    {
		for (int i = 1; i <= maxI; i++)
		{
			lastSum += rb.countBlack(i, hh, n);
		}
    }
    cout << lastSum;

    return 0;
}

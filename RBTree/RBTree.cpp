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
    int leftNodeCount = i - 1;
    int rightNodeCount = N - i;
    if (leftNodeCount < 0 || rightNodeCount < 0)
    {
        return 1;
    }
    if (N == 3 || N == 1)
    {
		cout << "countRed returns 0" << endl; 
        return 0;
    }
    if (N == 2)
    {
		cout << "countRed returns 1" << endl; 
        return 1;
    }
    if (leftNodeCount < rightNodeCount)
    {
		int countLeft = countBlack(i - 1, h, leftNodeCount);
		int countRight = countBlack(N - i, h, rightNodeCount);
        cout << "countRed returns " << countLeft * countRight << endl;
        return countLeft * countRight;
    }
    if (leftNodeCount == rightNodeCount)
    {
		int countLeft = countBlack(i - 1, h, leftNodeCount) + countRed(i - 1, h, leftNodeCount);
        cout << "countRed returns " << countLeft * (countLeft + 1) / 2 << endl;
        return countLeft * (countLeft + 1) / 2;
    }
    if (leftNodeCount > rightNodeCount)
    {
        cout << "Debug: error" << endl; 
        return 0;
    }
}

int rb_tree::countBlack(int i, int h, int N)
{
    int leftNodeCount = i - 1;
    int rightNodeCount = N - i;
    if (leftNodeCount < 0 || rightNodeCount < 0)
    {
        return 1;
    }
    if (N == 3 || N == 1)
    {
		cout << "countBlack returns 0" << endl; 
        return 0;
    }
    if (N == 2)
    {
		cout << "countBlack returns 1" << endl; 
        return 1;
    }
    if (leftNodeCount < rightNodeCount)
    {
		int countLeft = countBlack(i - 1, h - 1, leftNodeCount) + countRed(i - 1, h - 1, leftNodeCount);
		int countRight = countBlack(N - i, h - 1, rightNodeCount) + countRed(N - i, h - 1, rightNodeCount);
        cout << "countBlack returns " << countLeft * countRight << endl;
        return countLeft * countRight;
    }
    if (leftNodeCount == rightNodeCount)
    {
		int countLeft = countBlack(i - 1, h - 1, leftNodeCount) + countRed(i - 1, h - 1, leftNodeCount);
        cout << "countBlack returns " << countLeft * (countLeft + 1) / 2 << endl;
        return countLeft * (countLeft + 1) / 2;
    }
    if (leftNodeCount > rightNodeCount)
    {
        cout << "Debug: error" << endl; 
        return 0;
    }
}

int main()
{
    rb_tree rb;
    unsigned int n;
    std::cin >> n;
    unsigned int h = 2 * log2(n+1);

    int lastSum = 0;
    int maxI = (n + 1) / 2;
    for (int hh = 1; hh < h; hh++)
    {
		for (int i = 1; i <= maxI; i++)
		{
			lastSum += rb.countBlack(i, hh, n);
		}
    }
    cout << lastSum;


    return 0;
}

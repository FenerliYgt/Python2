#include <iostream>

using namespace std;

void initImage(int x[][10]);
void printClusterIndices(const int x[][10], const int code);

int main()
{
	int I[10][10] = {};

	cout << "I:" << endl;
	initImage(I);

	int code = 1;
	for (code; code <= 6; code++)
	{
		cout << "\nCluster for color code " << code << ":\n";
		printClusterIndices(I, code);
	}

	return 0;
}

void initImage(int x[][10])
{
	int i, j;
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			if (i < 5 && j < 6)
			{
				x[i][j] = 1;
			}
			else if (i < 5 && j>5)
			{
				x[i][j] = 2;
			}
			else if (i > 4 && i < 7 && j < 6)
			{
				x[i][j] = 3;
			}
			else if (i > 4 && i < 7 && j>5)
			{
				x[i][j] = 2;
			}
			else if (i > 6 && i <= 7 && j < 6)
			{
				x[i][j] = 3;
			}
			else if (i > 6 && i <= 7 && j > 5)
			{
				x[i][j] = 5;
			}
			else if (i > 7 && i <= 8 && j < 6)
			{
				x[i][j] = 4;
			}
			else if (i > 7 && i <= 8 && j > 5)
			{
				x[i][j] = 5;
			}
			else if (i > 8 && i <= 9 && j < 6)
			{
				x[i][j] = 6;
			}
			else if (i > 8 && i <= 9 && j > 5)
			{
				x[i][j] = 6;
			}
			cout << x[i][j] << "\t";
		}
		cout << endl;
	}
}

void printClusterIndices(const int x[][10], const int code)
{
	int i, j;
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			if (x[i][j] == code)
			{
				int index = i * 10 + j + 1;
				cout << "Pixel Index: " << index << " (i=" << i << ", j=" << j << ")" << endl;
			}
		}
	}
}
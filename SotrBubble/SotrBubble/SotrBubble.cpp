#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector <int>& AAA)
{
int length = AAA.size();

	for (int i = 0; i < length-1; i++)
	{
		for (int j = 0; j < length-1-i; j++)
		{
			if (AAA[j] > AAA[j + 1])
			{
				swap(AAA[j], AAA[j + 1]);
			}
		}
	}


//	for (int z = 0; z < length; z++)
//	{
//		cout << AAA[z] << " ";
//	}
};

void print(vector <int>& AAA)
{
	for (const auto& x : AAA)
	{
		cout << x << " ";
	}
}


int main()
{
	vector<int> ZZZ{ 9, 3, 4, 8, 10, 7, 10, 30, 4, 1 };
	bubbleSort(ZZZ);
	print(ZZZ);
}

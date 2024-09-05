#include <iostream>
#include <vector>

using namespace std;

void quickSort(int* tab, int left, int right)
{
    if (right <= left) return;

    int i = left - 1;
    int j = right + 1;

    int pivot = tab[(left + right) / 2];

    while (1)
    {
        while (pivot > tab[++i]);

        while (pivot < tab[--j]);

        if (i <= j)
            swap(tab[i], tab[j]);
        else break;
    }

    if (left < j)
        quickSort(tab, left, j);

    if (right > i)
        quickSort(tab, i, right);
}


int main()
{
    int *tab, size;

    cout << "Insert the size of array" << endl;
    cin >> size;

    tab = new int[size];

    for (int i = 0; i < size; i++)
    {
        cout << "Insert the number for " << i + 1 << " window in the array" << endl;
        cin >> tab[i];
    }

    quickSort(tab, 0, size - 1);

    for (int i = 0; i < size; i++)
        cout << tab[i] << " ";

    cin.ignore();
    cin.get();
    return 0;
}

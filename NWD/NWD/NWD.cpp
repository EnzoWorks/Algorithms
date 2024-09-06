#include <iostream>
#include <vector>

using namespace std;

int NWD(int First, int Second)
{

    if (First < Second)
        swap(First, Second);

    int Mod = First % Second;

    if (Mod > 0)
    {
        First = Mod;

        NWD(First, Second);
    }

    return Mod;
}

int main()
{
    int x, y;

    cout << "Insert two numbers: " << endl;

    cin >> x >> y;

    cout << "NWD(" << x <<"," << y << ") = " << NWD(x, y);
}

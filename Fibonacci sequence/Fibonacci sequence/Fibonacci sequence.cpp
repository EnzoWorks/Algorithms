#include <iostream>

using namespace std;

void AllFibonacciNumbers(int n)
{
    unsigned long a = 0, b = 1;

    for (int i = 0; i < n; i++)
    {
        cout << b << " ";
        b += a;
        a = b - a;
    }
}


int main()
{
    int n;

    cout << "How many numbers of Fibonacci sequence do you want to see: ";
    cin >> n;

    AllFibonacciNumbers(n);

    return 0;
}

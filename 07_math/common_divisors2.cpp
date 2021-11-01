//
// Created by Hariharan Ragothaman on 11/1/21.
//

#include <iostream>
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int cnt[1000001]; //stores count of divisors

int main()
{
    ENABLEFASTIO();


    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a; cin >> a;
        for (int j = 1; j*j <= a; j++)
        {
            if(a % j == 0)
            {
                cnt[j]++;
                if (j != a / j) cnt[a / j]++;
                // the divisor and quotient are both divisors of a
            }
        }
    }
    for (int i = 1000000; i >= 1; i--)
    {
        if(cnt[i] >= 2)
        {
            cout << i;
            break;
        }
    }
    return 0;
}

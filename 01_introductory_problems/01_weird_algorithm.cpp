#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif

int main()
{
    ENABLEFASTIO();
    long long int n;
    cin >> n;
    cout << n << " ";
    while(n != 1)
    {
        if(n&1)
            n = n*3 + 1;
        else
            n /= 2;
        cout << n << " ";
    }
    cout << endl;
    return 0;
}
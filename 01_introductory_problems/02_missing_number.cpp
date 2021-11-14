#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

//#define LOCAL
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
    vector<long long int> arr(n, 0);

    long long int total = 0;
    for(int i=0; i<n; i++)
    {
        cin >> arr[i];
        total += arr[i];
    }
    cout << ((n*(n+1) >> 1) - total) << endl;
    return 0;
}
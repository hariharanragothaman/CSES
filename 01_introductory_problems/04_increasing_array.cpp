//
// Created by Hariharan Ragothaman on 11/14/21.
//

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
    for(int i=0; i<n; i++) cin >> arr[i];

    long long int moves = 0;
    for(int i=1; i<n; i++)
    {
        if (arr[i] < arr[i - 1])
        {
            long long int diff = abs(arr[i] - arr[i - 1]);
            arr[i] += diff;
            moves += diff;
        }
    }
    cout << moves << endl;
    return 0;
}
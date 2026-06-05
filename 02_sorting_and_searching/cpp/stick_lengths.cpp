//
// Created by Hariharan Ragothaman on 11/1/21.
//

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

// GODSPEED
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#include<bits/stdc++.h>
using namespace std;


#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
#endif


int main()
{
    ENABLEFASTIO();
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i=0; i<n; i++) cin>> arr[i];
    sort(arr.begin(), arr.end());

    int median = n%2 ? arr[n/2] : (arr[n/2] + arr[n/2-1]) / 2;

    long long result = 0;
    for(int i=0; i<n; i++)
    {
        result += abs(median-arr[i]);
    }
    cout << result;
    return 0;
}

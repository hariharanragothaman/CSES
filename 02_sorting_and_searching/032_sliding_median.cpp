//
// Created by Hariharan Ragothaman on 11/14/21.
//

/**********  SLIDING WINDOW  ***********/

#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define endl "\n"
#define int long long

//#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif


/*
 *  Intiution explanation
 *  We want to compute something, here median,
 *  for every window of elements....
 */

int32_t main()
{
    ENABLEFASTIO();
    int n;
    int k;
    cin >> n >> k;

    vector<int> arr(n, 0);
    for(int i=0; i<n; i++) cin >> arr[i];



    return 0;
}



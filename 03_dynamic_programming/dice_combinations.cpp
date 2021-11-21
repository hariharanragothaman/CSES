//
// Created by Hariharan Ragothaman on 11/17/21.
//

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

int32_t main()
{
    int mod = 1e9+7;
    int n;
    cin >> n;
    vector<int> dp(n+1,0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= 6 && i-j >= 0; j++)
        {
            dp[i] = (dp[i] + dp[i-j]) % mod;
        }
    }
    cout << dp[n] << endl;
    return 0;
}
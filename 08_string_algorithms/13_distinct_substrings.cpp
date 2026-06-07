//
// Created by Hariharan Ragothaman on 11/15/21.
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
    ENABLEFASTIO();
    string s;
    cin >> s;
    // Starting rolling hash
    int n = s.size();

    const int p = 31;
    const int m = 1e9 + 9;
    vector<int> p_pow(n);
    p_pow[0] = 1;
    for (int i = 1; i < n; i++)
        p_pow[i] = (p_pow[i-1] * p) % m;


    for(auto c: p_pow)
        cout << c << " " ;
    cout  << endl;

    vector<long long> h(n + 1, 0);
    for (int i = 0; i < n; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

    int cnt = 0;
    for (int l = 1; l <= n; l++)
    {
        set<long long> hs;
        for (int i = 0; i <= n - l; i++)
        {
            long long cur_h = (h[i + l] + m - h[i]) % m;
            cur_h = (cur_h * p_pow[n-i-1]) % m;
            hs.insert(cur_h);
        }
        cnt += hs.size();
    }

    cout << cnt;
    return 0;
}

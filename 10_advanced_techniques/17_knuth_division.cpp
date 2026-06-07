/**
 * File              : 17_knuth_division.cpp
 * Problem           : Knuth Division
 * Section           : Advanced Techniques
 * Status            : UNSOLVED (placeholder)
 */

#include "bits/stdc++.h"
#include <numeric>
using namespace std;

#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
#else
#endif

#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int long long
#define stars cout << "********************************" << endl;
#define debug(a)  cout << a << endl;
#define MOD 1000000007
#define all(x) x.begin(), x.end()

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

void solve()
{
    // TODO: not solved
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    T = 1;
    //cin >> T;
    while(T--)
        solve();
}

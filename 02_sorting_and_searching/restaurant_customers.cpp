//
// Created by Hariharan Ragothaman on 10/29/21.
//
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

// GODSPEED
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#include<bits/stdc++.h>
using namespace std;

void solve(vector<pair<int, int>>& A, int& n)
{
    vector<pair<int, int>> linesweep;
    vector<int> start, end;
    for(auto c: A)
    {
        linesweep.emplace_back(make_pair(c.first, 1));
        linesweep.emplace_back(make_pair(c.second, -1));
    }

    std::sort(linesweep.begin(), linesweep.end());

    int count = 0;
    int tmp = 0;

    for(auto c: linesweep)
    {
        tmp += c.second;
        count = max(tmp, count);
    }
    cout << count << endl;
}

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
    vector<pair<int, int>> arr;
    int a = 0;
    int b = 0;
    while (n > 0)
    {
        cin >> a >> b;
        arr.emplace_back(make_pair(a, b));
        n--;
    }
    solve(arr, n);

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

// GODSPEED

bool sortBySecond(const pair<int,int> &a, const pair<int,int> &b)
{
    return (a.second < b.second);
}

void solve()
{
    int n;
    int x, y;
    int current_end = 0;
    int total = 0;
    vector<pair<int, int>> arr;
    cin >> n;
    while(n--)
    {
        cin >> x >> y;
        arr.emplace_back(make_pair(x, y));
    }

    sort(arr.begin(), arr.end(), sortBySecond);

    for(auto c: arr)
    {
        if(c.first >= current_end)
        {
            current_end = c.second;
            total++;
        }
    }
    cout << total;
}

//#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

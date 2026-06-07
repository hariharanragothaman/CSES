#include <bits/stdc++.h>
using namespace std;

// GODSPEED

void solve(vector<pair<int, int>>& A, int& n)
{
    vector<pair<int, int>> linesweep;
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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

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

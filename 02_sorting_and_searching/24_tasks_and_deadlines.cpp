#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    multimap<long int, long int> duration_deadlines;
    long long int duration;
    long long int deadline;
    for(int i=0; i<n; i++)
    {
        cin >> duration >> deadline;
        duration_deadlines.insert(make_pair(duration, deadline));
    }

    long long int finish_time = 0;
    long long int reward = 0;
    for(auto c: duration_deadlines)
    {
        finish_time += c.first;
        reward += (c.second - finish_time);
    }

    cout << reward << endl;

    return 0;
}

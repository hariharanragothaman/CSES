#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n, m;
    cin >> n >> m;
    int u{}, v{};
    vector<vector<int>> G(n+1);
    for(int i=0; i<m; i++)
    {
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    int start = 1;

    deque<pair<int, int>> Q;
    Q.push_back({start, 0});

    vector<bool> visited(n+1, 0);
    visited[start] = true;

    vector<int> P(n+1, -1);

    while(!Q.empty())
    {
        auto [node, distance] = Q.front(); Q.pop_front();
        if(node == n)
        {
            cout << distance + 1 << endl;
            break;
        }
        for(auto nei: G[node])
        {
            if(!visited[nei])
            {
                visited[nei] = true;
                P[nei] = node;
                Q.push_back({nei, distance + 1});
            }
        }
    }
    if(P[n] == -1)
    {
        cout << "IMPOSSIBLE" << endl;
    }
    else
    {
        int tmp = n;
        vector<int> path;
        path.push_back(n);
        while(P[tmp] != -1)
        {
            path.push_back(P[tmp]);
            tmp = P[tmp];
        }
        reverse(path.begin(), path.end());
        for(auto c: path)
        {
            cout << c << " ";
        }
        cout << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

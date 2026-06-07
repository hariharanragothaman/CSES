#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> C;

public:
void connectedComponents(vector<vector<int>>& G, int start, vector<bool>& visited)
{
    deque<int> Q = {start};
    visited[start] = true;
    vector<int> component;
    while(!Q.empty())
    {
        auto node = Q.back(); Q.pop_back();
        component.push_back(node);
        for(auto c: G[node]) if(!visited[c]) visited[c] = true, Q.push_back(c);
    }
    C.push_back(component);
}

void solve()
{
    int n, m;
    cin >> n >> m;

    /* Creating the adjacency matrix */
    int u{}, v{};
    vector<vector<int>> G(n+1);
    for(int i=0; i<m; i++)
    {
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    /* Calculating Connected Components*/
    int cnt{};
    vector<bool> visited(n+1, 0);
    for(int i=1; i<=n; i++)
    {
        if(!visited[i])
        {
            connectedComponents(G, i, visited);
            cnt++;
        }
    }

    // Number of roads to be constructed is component - 1
    cout << cnt - 1 << endl;
    vector<int> result;
    for(auto comp: C)
        result.push_back(comp.front());
    for(int i=0; i<result.size()-1; i++)
    {
        cout << result[i] << " " << result[i+1] << "\n";
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

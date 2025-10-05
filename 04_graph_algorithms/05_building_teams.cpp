/*
 *    FOCUS + DETERMINATION + SHEER-WILL
 */

#ifndef ONLINE_JUDGE
#include "headers.h"
#else
#include "bits/stdc++.h"
    #include "sys/stat.h"
    using namespace std;
#endif

using i64 = long long;
using u64 = unsigned long long;
using i32 = int;
using u32 = unsigned int;
using ld  = long double;
//--------------------------
using vi   = vector<int>;
using vl   = vector<long long>;
using vvi  = vector<vector<int>>;
using vvl  = vector<vector<long long>>;
using pii  = pair<int,int>;
using pll  = pair<long long,long long>;
using vpii = vector<pii>;
using vpll = vector<pll>;
using iset = set<int>;
using imap = map<int,int>;
//--------------------------

inline void fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

class Solution
{
    vector<vector<int>> C;

public:
    void solve()
    {
        int n, m;
        cin >> n >> m;

        vector<vector<int>> G(n+1);
        int u, v;
        for(int i=0; i<m; i++)
        {
            cin >> u >> v;
            G[u].push_back(v);
            G[v].push_back(u);
        }

        vector<int> color(n+1, 0); // 0=uncolored, 1/2 teams
        deque<int> Q;

        for(int node=1; node<=n; node++) // Maybe the graph is disconnected.
        {
            if(color[node]) continue; // Already colored
            color[node] = 1;
            Q.push_back(node);

            while(!Q.empty())
            {
                auto u = Q.front(); Q.pop_front();
                for(auto nei: G[u])
                {
                    if(!color[nei])
                    {
                        color[nei] = 3 - color[u];
                        Q.push_back(nei);
                    }
                    else if(color[nei] == color[u])
                    {
                        cout << "IMPOSSIBLE" << endl;
                        return;
                    }
                }
            }
        }

        for(int i=1;i<=n;i++)
        {
            if(i>1) cout << ' ';
            cout << color[i];
        }
        cout << '\n';
    }
};

int main()
{
    fast_io();
    int T = 1;
    Solution object;
    while(T--)
    {
        object.solve();
        ldebug();
    }
    return 0;
}

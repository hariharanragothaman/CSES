/*
 *    FOCUS + DETERMINATION + SHEER-WILL
 */

/*
 * Note:
 * Straightforward BFS, remember to have a parent-map for the path.
 *
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
public:
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
};

int main()
{
    fast_io();
    int T = 1;
    Solution object;
    while(T--)
    {
        object.solve();
    }
    return 0;
}

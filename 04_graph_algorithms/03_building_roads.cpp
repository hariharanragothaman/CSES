/*
 *    FOCUS + DETERMINATION + SHEER-WILL
 */

/*
 * Note:
 * Count the number connected components - Very straightforward
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

inline bool fileExists (const std::string& name)
{
    struct stat buffer;
    return (stat (name.c_str(), &buffer) == 0);
}

inline void ldebug()
{
    if(fileExists("data.in"))
        cout << string(25, '-');
    cout << endl;
}

class Solution
{
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

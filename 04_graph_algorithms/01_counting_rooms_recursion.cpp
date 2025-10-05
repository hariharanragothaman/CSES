/*
 *    FOCUS + DETERMINATION + SHEER-WILL
 */

#ifndef ONLINE_JUDGE
#include "../headers.h"
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
    void dfs(vector<vector<char>>& A, int i, int j, int n, int m)
    {
        if(A[i][j] != '.')
        {
            return;
        }
        A[i][j] = '#';
        vector<pair<int, int>> nei = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
        for(auto [x, y]: nei)
        {
            int nx = i + x;
            int ny = j + y;
            if(nx < n and nx >= 0 and ny < m and ny >= 0)
            {
                dfs(A, nx, ny, n, m);
            }
        }
    }
    void solve()
    {
        int n, m;
        cin >> n >> m;
        char ch;
        vector<vector<char>> A(n, vector<char>(m, 0));
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                cin >> ch;
                A[i][j] = ch;
            }
        }

        int rooms{};
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(A[i][j] == '.')
                {
                    dfs(A, i, j, n, m);
                    rooms++;
                }
            }
        }
        cout << rooms << endl;
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

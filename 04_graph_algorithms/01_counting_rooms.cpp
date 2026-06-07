#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<char>>& A, int i, int j, int n, int m)
{
    deque<pair<int, int>> Q;
    Q.push_back(make_pair(i, j));
    pair<int, int> node;

    int nr, nc;

    while(!Q.empty())
    {
        node = Q.back();
        Q.pop_back();
        A[node.first][node.second] = '#';   // Mark node as visited

        nr = node.first;
        nc = node.second;
        vector<pair<int, int>> moves = {{1, 0}, {0, -1}, {0, 1}, {-1, 0}};
        for(auto [dx, dy]: moves)
        {
            dx += nr;
            dy += nc;
            if (0 <= dx && dx < n && dy >= 0 && dy < m)
                if (A[dx][dy] == '.')
                    Q.push_back(make_pair(dx, dy));
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
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

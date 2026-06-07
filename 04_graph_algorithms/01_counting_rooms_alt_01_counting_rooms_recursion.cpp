#include <bits/stdc++.h>
using namespace std;

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
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

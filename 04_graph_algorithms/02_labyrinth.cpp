#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n, m;
    cin >> n >> m;
    pair<int, int> s{}, t{};

    vector<vector<char>> A(n, vector<char>(m, ' '));
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            cin >> A[i][j];
            if(A[i][j] == 'A') s = {i, j};
            if(A[i][j] == 'B') t = {i, j};
        }
    }

    vector<vector<char>> P(n, vector<char>(m, 0));
    deque<pair<int, int>> Q;

    P[s.first][s.second] = 'S'; // sentinel marking
    Q.push_back(s);
    const std::pair<int, int> moves[] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    bool path_exists = false;

    while(!Q.empty() && !path_exists)
    {
        auto [x, y] = Q.front();
        Q.pop_front();
        for(auto [dx, dy]: moves)
        {
            int nx = x + dx;
            int ny = y + dy;

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (P[nx][ny] != 0) continue;
            if (A[nx][ny] == '#') continue;

            char direction;
            if(dx == -1 && dy == 0 ) direction = 'U';
            else if(dx == 0 && dy == -1 ) direction = 'L';
            else if(dx == 1 && dy == 0 ) direction = 'D';
            else if(dx == 0 && dy == 1 ) direction = 'R';

            P[nx][ny] = direction;
            Q.push_back({nx, ny});
            if (nx == t.first && ny == t.second)
            {
                path_exists = true;
                break;
            }
        }
    }

    if(path_exists)
    {
        string path;
        int x = t.first, y = t.second;
        while (P[x][y] != 'S') {
            char d = P[x][y];
            path.push_back(d);
            // move backwards: invert the step we took to enter (x,y)
            if (d == 'U') x += 1;
            else if (d == 'D') x -= 1;
            else if (d == 'L') y += 1;
            else if (d == 'R') y -= 1;
        }
        reverse(path.begin(), path.end());
        cout << "YES\n" << (int)path.size() << "\n" << path << "\n";
    }
    else
    {
        cout << "NO\n";
    }

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}

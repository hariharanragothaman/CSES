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
public:
    void get_shortest_path(vector<vector<char>>& A, int R, int C, pair<int, int> start)
    {
        deque<tuple<int, int, int, string>> Q;
        Q.push_back(make_tuple(0, start.first, start.second, ""));
        const std::pair<int, int> moves[] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

        int shortest_distance = INT_MAX;
        string result_path = "";
        bool path_exists = false;
        A[start.first][start.second] = '#';

        while(!Q.empty())
        {
            auto [dist, x, y, path] = Q.front();
            Q.pop_front();

            for(auto [dx, dy]: moves)
            {
                string direction;
                if(dx == -1 && dy == 0 ) direction = "U";
                else if(dx == 0 && dy == -1 ) direction = "L";
                else if(dx == 1 && dy == 0 ) direction = "D";
                else if(dx == 0 && dy == 1 ) direction = "R";

                int nx = x + dx;
                int ny = y + dy;

                if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;

                if (0 <= nx && nx < R && ny >= 0 && ny < C)
                {
                    if(A[nx][ny] == 'B')
                    {
                        path_exists = true;
                        if(dist + 1 < shortest_distance)
                        {
                            shortest_distance = dist + 1;
                            result_path = path + direction;
                            break;
                        }
                    }

                    else if(A[nx][ny] == '.')
                    {
                        A[nx][ny] = '#';
                        Q.push_back(make_tuple(dist+1, nx, ny, path+direction));
                    }
                }
            }
        }

        if(path_exists)
        {
            cout << "YES" << endl;
            cout << shortest_distance << endl;
            cout << result_path << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    void solve()
    {
        int R, C;
        cin >> R >> C;
        pair<int, int> start;
        vector<vector<char>> A(R, vector<char>(C, ' '));
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                cin >> A[i][j];
                if(A[i][j] == 'A')
                {
                    start.first = i;
                    start.second = j;
                }
            }
        }

        get_shortest_path(A, R, C, start);
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

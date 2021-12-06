#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

const std::pair<int, int> moves[] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void dfs(vector<vector<char>>& A, int& r, int& c, int& R, int& C)
{
    deque<pair<int, int>> Q;
    Q.push_back(make_pair(r, c));
    pair<int, int> node;

    int nr, nc;

    while(!Q.empty())
    {
        node = Q.back();
        Q.pop_back();
        A[node.first][node.second] = '#';   // Mark node as visited

        nr = node.first;
        nc = node.second;

        for(auto [dx, dy]: moves)
        {
            dx += nr;
            dy += nc;
            if (0 <= dx && dx < R && dy >= 0 && dy < C)
                if (A[dx][dy] == '.')
                    Q.push_back(make_pair(dx, dy));
        }
    }
}

//#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif

int main()
{
    ENABLEFASTIO();
    int R, C;
    cin >> R >> C;
    vector<vector<char>> A;

    string s;
    vector<char> tmp;
    for (int i = 0; i < R; i++)
    {
        cin >> s;
        for(auto c: s) tmp.push_back(c);
        A.push_back(tmp);
        tmp.clear();
    }

    int rooms = 0;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (A[i][j] == '.')
            {
                dfs(A, i, j, R, C);
                rooms++;
            }

    cout << rooms << endl;


    return 0;
}
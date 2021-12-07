#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

//#define LOCAL
#ifdef LOCAL
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
// Submit to Online Judge
#endif

const std::pair<int, int> moves[] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void get_shortest_path(vector<vector<char>>& A, int& R, int& C, pair<int, int>&start)
{
    deque<tuple<int, int, int, string>> Q;
    Q.push_back(make_tuple(0, start.first, start.second, ""));

    int shortest_distance = INT_MAX;
    string result_path = "";

    int dist;
    int x, y;
    string path;
    bool pathExists = false;

    while(Q.size() > 0)
    {
        tie(dist, x, y, path) = Q.front();
        Q.pop_front();

        for(auto [dx, dy]: moves)
        {
            string direction;
            if(dx == -1 && dy == 0 ) direction = "U";
            else if(dx == 0 && dy == -1 ) direction = "L";
            else if(dx == 1 && dy == 0 ) direction = "D";
            else if(dx == 0 && dy == 1 ) direction = "R";

            dx += x;
            dy += y;
            if (0 <= dx && dx < R && dy >= 0 && dy < C)
            {
                if(A[dx][dy] == 'B')
                {
                    pathExists = true;
                    if(dist+1 < shortest_distance)
                    {
                        shortest_distance = dist + 1;
                        result_path = path + direction;
                    }
                }

                else if(A[dx][dy] == '.')
                {
                    A[dx][dy] = '#';
                    Q.push_back(make_tuple(dist+1, dx, dy, path+direction));
                }

            }
        }
    }

    if(pathExists)
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


int main()
{
    ENABLEFASTIO();
    int R, C;
    cin >> R >> C;

    pair<int, int> start;
    vector<vector<char>> A(R, vector<char>(C));

    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
        {
            cin >> A[i][j];
            if(A[i][j] == 'A')
                start.first = i, start.second = j;
        }

    get_shortest_path(A, R, C, start);
    return 0;

}
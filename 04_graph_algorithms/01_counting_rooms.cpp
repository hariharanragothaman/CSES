//
// Created by Hariharan Ragothaman on 11/28/21.
//

#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

vector<vector<int>> get_neighbours(int r, int c, int R, int C)
{
    vector<vector<int>> directions = {{r+1, c}, {r, c+1}, {r-1, c}, {r, c-1}};
    vector<vector<int>> nei;
    for(auto d: directions)
    {
        if(0 <= d[0] && d[0]< R && d[1] >= 0 && d[1] < C)
            nei.push_back({d[0], d[1]});
    }
    return nei;
}


void dfs(vector<vector<char>>& A, int& r, int& c, int& R, int& C)
{
    deque<pair<int, int>> Q;
    Q.push_back(make_pair(r, c));
    pair<int, int> node;

    while(!Q.empty())
    {
        node = Q.back();
        Q.pop_back();
        A[node.first][node.second] = '#';   // Mark node as visited
        vector<vector<int>> nei = get_neighbours(node.first, node.second, R, C);
        for(auto nr: nei)
            if(A[nr[0]][nr[1]] == '.')
                Q.push_back(make_pair(nr[0], nr[1]));
    }
}


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
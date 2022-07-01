
/*
 *  This question is to find the lowest common ancestor
 *  There are totally 5 ways, to determine the (LCA)
 *
 *  Method1: Using Euler tour and 2 additional arrays
 *  Method2: Binary lifting
 *  Method3: Farach-Colton and Bender Algorithm
 *  Method4: Solve RMQ by finding LCA
 *  Method5: Tarjan's Offline Algorithm
 */

#include "bits/stdc++.h"
using namespace std;



void solve(unordered_map<int, vector<int>>& G, int& a, int& b)
{
    // Generate euler tour, heights array and first array


}


int main()
{
    int n, q;
    cin >> n >> q;
    int root  = 1;

    vector<int> parents(0, n);
    unordered_map<int, vector<int>> G;

    for(int i=2; i<n; i++)
    {
        cin >> parents[i];
        G[parents[i]].push_back(i);
    }


    while(q--)
    {
        int a, b;
        cin >> a >> b;
        solve(G, a, b);
    }

    return 0;
}

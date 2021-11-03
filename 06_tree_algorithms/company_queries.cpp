/*
 * Concept: Binary Lifting
 * Side Concept: Any number can be represented as a power of 2 (Applying DP here)
 * References:
 * https://cses.fi/problemset/task/1687/
 * https://usaco.guide/plat/binary-jump
 * https://www.youtube.com/watch?v=MOy4UDjN8DM
 * https://aryansh.gitbook.io/informatics-notes/binary-lifting/binary-lifting-gold-part-1
 */

// GCC Optimizations
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

#include "bits/stdc++.h"
using namespace std;

#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int jmp(int k, int x, vector<vector<int>>& UP)
{
    /* Get the kth ancestor of x */
    /*
     *  Here we find how the number can be represented as
     *  a sum of powers of 2
     *  so if k = 13 for example 1101 in binary 2^0, 2^2, 2^3
     *  It's set at bit 1 - at 0,2,3 locations.
     *  So it will enter the if conditions when i = 0, 2, 3..
     */
    int MAX_POWER = UP.size();
    for(int i=0; i<MAX_POWER; i++)
    {
        if( (k >> i) & 1 )
        {
            cout << "Entering if condition " << i << endl;
            x = UP[i][x];
        }
    }
    return x ?: -1;
}

void solve(vector<int>& arr, int& n, int& employee, int& k)
{
    // Creating / Pre-computing the matrix for binary-lifting
    vector<vector<int>> UP;
    int MAX_POWER = ceil(log2(n));
    UP.assign(MAX_POWER+1, vector<int>(n+1));

    /*
     * UP [i][j] is the 2^ith ancestor of node j
     * ROWS - Powers of 2 from 1,2,4 etc
     * COLS - Nodes
     */

    // So for the first row - let's fill in the values
    for(int j=2; j<n+1; j++)
        UP[0][j] = arr[j];

    // Now filling in for the rest of the rows...
    for(int i=1; i<MAX_POWER; i++)
    {
        for(int j=1; j< n+1; j++)
        {
            UP[i][j] = UP[i-1][UP[i-1][j]];
        }
    }

    int ans = jmp(k, employee, UP);
    cout << ans << endl;
}

int main()
{
    ENABLEFASTIO();
    int n, queries;
    cin >> n >> queries;
    vector<int> arr(n+1, 0);
    for(int i=2; i<n+1; i++)
        cin >> arr[i];

    int employee;
    int k;
    while(queries--)
    {
        cin >> employee >> k;
        solve(arr, n, employee, k);
    }
    return 0;
}
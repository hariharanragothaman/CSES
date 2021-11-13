//
// Created by Hariharan Ragothaman on 11/12/21.
//
// Ref: https://usaco.guide/problems/cses-1620-factory-machines/solution

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

/*
 *  For each product you need to make
 *  ans / k[i] jumps to make a product
 *  So we can binary search for the ans across the entire sample space.
 */

int main()
{
    ENABLEFASTIO();
    int n;
    int t;
    cin >> n >> t;

    vector<int> k(n, 0);
    for(int i=0; i<n; i++)
        cin >> k[i];

    long long low = 0;
    long long high = 1e18;
    long long ans = 0;

    while(low <= high)
    {
        long long pivot =(low + high) >> 1;
        long long sum = 0;
        for(int i=0; i<n; i++)
        {
            sum += (pivot / k[i]);
            if(sum >= t)
                break;
        }

        if(sum >= t)
        {
            ans = pivot;
            high = pivot -1;
        }
        else
        {
            low = pivot + 1;
        }
    }

    cout << ans << endl;
    return 0;
}


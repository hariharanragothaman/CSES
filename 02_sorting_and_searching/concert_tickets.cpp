//
// Created by Hariharan Ragothaman on 11/12/21.
//

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

int main()
{
    ENABLEFASTIO();
    int n, m;
    cin >> n >> m;
    // We can use multiset since it will be sorted and will use duplicates
    multiset<int> ticketprice;
    vector<int> customer(m, 0);
    int h;
    for(int i=0; i<n; i++)
    {
        cin >> h;
        ticketprice.insert(h);
    }

    for(int i=0; i<m; i++)
    {
        cin >> customer[i];
        auto it = ticketprice.upper_bound(customer[i]);
        if(it == ticketprice.begin())
            cout << -1 << endl;
        else
        {
            cout << *(--it) << endl;
            ticketprice.erase(it);
        }
    }

    return 0;
}

//
// Created by Hariharan Ragothaman on 11/14/21.
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
    int n;
    cin >> n;
    if(n==1)
        cout << 1 << endl;
    else if(n==4)
    {
        vector<int> res = {2, 4, 1, 3};
        for(auto c: res) cout << c << " ";
        cout << endl;
    }
    else if(n < 5)
    {
        cout << "NO SOLUTION" << endl;
    }
    else
    {
        vector<int> odd, even;
        for(int i=n; i>0; i--)
        {
            if(i&1)
                odd.push_back(i);
            else
                even.push_back(i);
        }
        for(auto c: odd)
            cout << c << " ";
        for(auto c: even)
            cout << c << " ";
        cout << endl;
    }
    return 0;
}
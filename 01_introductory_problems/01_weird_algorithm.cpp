/**
 * File              : 01_weird_algorithm.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 12.02.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
#include <numeric> 
using namespace std;

#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
#else
#endif


#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int long long
#define stars cout << "********************************" << endl;
#define debug(a)  cout << a << endl;
#define MOD 1000000007
#define all(x) x.begin(), x.end()

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}
void solve()
{
	int n; 
	cin >> n;
	while(n != 1)
	{
		cout << n << " ";
		if((n & 1) == 0)
		{
			n >>= 1;
		}
		else 
		{
			n = n*3 + 1;
		}
	}
	cout << 1 << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    T = 1;
    //cin >> T;
    while(T--)
        solve();
}

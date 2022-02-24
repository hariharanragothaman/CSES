/*
* @Author: Hariharan Ragothaman
* @Date:   2022-01-06 20:55:12
* @Last Modified by:   Hariharan Ragothaman
* @Last Modified time: 2022-01-08 14:06:10
*/

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
#define cin  i_data
#define cout o_data
#else
#endif

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

void solve()
{
	int n, k;
	cin >> n >> k;
	vector<int> A(n, 0);
	for(int i=0; i<n; i++)
		cin >> A[i];

	bool fl = true;
	if(k&1)
		fl = false;

	for(int i=0; i<=n-k; i++)
	{
		vector<int> C; 
		for(int j=i; j<i+k; j++)
			C.emplace_back(A[j]);
		sort(C.begin(), C.end());
		if(fl==false)
		{
			cout << C[k/2] << " ";
		}
		else
		{
			cout << min(C[k/2], C[k/2-1]) << " ";
		}
	}
	cout << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}






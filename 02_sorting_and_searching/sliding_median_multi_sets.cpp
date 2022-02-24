/*
* @Author: Hariharan Ragothaman
* @Date:   2022-01-08 14:15:35
* @Last Modified by:   Hariharan Ragothaman
* @Last Modified time: 2022-01-08 14:55:09
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

multiset<long long> up;
multiset<long long> low;
long long n, k;

void ins(long val){ // insert val into sets
	long a = *low.rbegin(); // current median
	if(a < val){
		up.insert(val);
		if(up.size() > k/2){
			low.insert(*up.begin());
			up.erase(up.find(*up.begin()));
		}
	}
	else{
		low.insert(val);
		if(low.size() > (k + 1)/2){
			up.insert(*low.rbegin());
			low.erase(low.find(*low.rbegin()));
		}
	}
}

void er(long val){ // erase from sets
	if(up.find(val) != up.end()) up.erase(up.find(val));
	else low.erase(low.find(val));
	if(low.empty()){
		low.insert(*up.begin());
		up.erase(up.find(*up.begin()));
	}
}

void solve()
{
	cin >> n >> k;
	vector<int> A(n, 0);
	for(int i=0; i<n; i++)
		cin >> A[i];

	// Using multi-sets, by default set is sorted.

	low.insert(A[0]);
	for(int i = 1; i < k; i++) 
		ins(A[i]);

	cout << *low.rbegin() << " ";

	for(long i = k; i < n; i++)
	{
		if(k == 1)
		{
			ins(A[i]);
			er(A[i - k]);
		}
		else
		{
			er(A[i - k]);
			ins(A[i]);
		}
		cout << *low.rbegin() << " ";
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






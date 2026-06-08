#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	int n {};
	cin >> n;
	int a = 0; 
	int sum = 0;  
	for(int i=0; i<n-1; i++) {
		cin >> a; 
		sum += a; 
	}
	cout << ((n*(n+1)) >> 1) - sum << endl;
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
	return 0; 
}

#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	int n {}; 
	cin >> n; 
	cout << n << " "; 
	while(n != 1) {
		if(n & 1) n = n * 3 + 1; 
		else n >>= 1; 
		cout << n << " ";
	}
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
	return 0; 
}

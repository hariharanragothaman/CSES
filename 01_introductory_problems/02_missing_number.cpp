#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	int n; 
	cin >> n; 
	vector<int> A(n, 0);
	int sum = 0;
	for(int i=0; i<n; i++) 
	{
		cin >> A[i];
		sum += A[i];
	}
	cout << ((n*(n+1)) >> 1) - sum << endl;
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

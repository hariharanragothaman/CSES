#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	int n; 
	cin >> n;
	vector<int> A(n, 0);
	for(int i=0; i<n; i++) cin >> A[i];
	int ans = 0; 
	for(int i=1; i<n; i++) 
	{
		if(A[i] < A[i-1])
		{
			int diff = abs(A[i] - A[i-1]);
			A[i] += diff;
			ans += diff;
		}
	}
	debug(ans);
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

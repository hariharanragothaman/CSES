#include <bits/stdc++.h>
using namespace std;
#define int long long

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

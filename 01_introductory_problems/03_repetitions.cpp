#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	string s; 
	cin >> s;
	int mx = 1;
	int cnt = 1;

	for(int i=1; i<s.size(); i++)
	{
		if(s[i] == s[i-1])
		{
			cnt++;
		}
		else 
		{
			cnt = 1;
		}
		mx = max(mx, cnt);
	}
	debug(mx);
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

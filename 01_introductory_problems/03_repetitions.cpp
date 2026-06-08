#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
	string s; 
	cin >> s; 
	int max_cnt = 1, curr_cnt = 1; 
	int n = s.size(); 
	
	for(int i=1; i<n; i++) {
		if(s[i] == s[i-1])
			curr_cnt++; 
		else {
			max_cnt = max(max_cnt, curr_cnt);
			curr_cnt = 1;
		}	
	}
	max_cnt = max(max_cnt, curr_cnt);
	cout << max_cnt << endl; 
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}

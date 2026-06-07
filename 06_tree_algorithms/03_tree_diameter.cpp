#include <bits/stdc++.h>
using namespace std;
#define int long long

void dfs(map<int, vector<int>>& G, int& n)
{

}

void solve()
{
	int n; 
	cin >> n; 
	vector<int> A(n+1, 0);
	for(int i=2; i<=n; i++)
		cin >> A[i];

	map<int, vector<int>> G; 
	G[1] = {};
	for(int j=2; j<n+1; j++)
		G[A[j]].push_back(j);

	dfs(G, n);
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

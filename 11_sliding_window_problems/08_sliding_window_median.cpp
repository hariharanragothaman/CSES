#include <bits/stdc++.h>
using namespace std;

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

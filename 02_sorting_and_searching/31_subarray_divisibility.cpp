#include <bits/stdc++.h>
using namespace std;
#define int long long

// #define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

void solve()
{
	int N;
	cin >> N;

	vector<long long> M(N);
	long long psums = 0;
	M[psums] = 1;
	for (int i = 0; i < N; i++) 
	{
		int a;
		cin >> a;
		psums += a;
		// Remember to account for negative sums
		M[(psums % N + N) % N]++;
	}

	// Printing the map
	
	for(auto c: M)
	{
		cout << c << " "; 
	}
	cout << endl;

	long long ans = 0;
	for (long long x : M) 
	{
		/*
		 * Calculating the # of pairs.
		 * This calculates the pairs without
		 * duplicates and reverse groups.
		 */
		ans += x * (x - 1) / 2;
	}
	cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

#include <bits/stdc++.h>
using namespace std;
#define int long long

// #define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

bool comparator(pair<int, int> A, pair<int, int> B)
{
	return (A.first < B.first);
}

// Putting all the odd numbers first
bool cmp(int a , int b)
{
	return a % 2 < b % 2;
}

bool revsort(int a, int b) 
{
	return a > b;
}

int compute(int a, int b, int c)
{
	return abs(a-b) + abs(a-c) + abs(b-c);
}

void solve()
{
	int ini_power, ini_health, n;
	cin >> ini_power >> ini_health >> n;
	vector<int> mpower(n, 0); 
	vector<int> mhealth(n, 0);

	for(int i=0; i<n; i++) cin >> mpower[i];
	for(int i=0; i<n; i++) cin >> mhealth[i];

}

int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

}

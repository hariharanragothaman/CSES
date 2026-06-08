#include <bits/stdc++.h>
using namespace std;

void solve() 
{
    int n {};
    cin >> n;
    set<int> s; 
    int a = 0; 
    for(int i=0; i<n; i++) {
        cin >> a; 
        s.insert(a);
    }
    cout << s.size() << endl; 
}

int32_t main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
	return 0; 
}

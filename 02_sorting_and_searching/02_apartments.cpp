#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m, k; 
    cin >> n >> m >> k;
    vector<int> desired_apt_size(n);
    vector<int> apt_size(m);
    for(int i=0; i<n; i++) {
        cin >> desired_apt_size[i];
    }
    for(int i=0; i<m; i++) {
        cin >> apt_size[i];
    }
    sort(desired_apt_size.begin(), desired_apt_size.end());
    sort(apt_size.begin(), apt_size.end());
    int count = 0; 

    int i = 0, j = 0; 
    while(i < n && j < m) {
        if(apt_size[j] < desired_apt_size[i] - k) 
            j++; 
        else if(apt_size[j] > desired_apt_size[i] + k)
            i++; 
        else {
            count++; 
            i++; 
            j++; 
        }
    }
    cout << count << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
